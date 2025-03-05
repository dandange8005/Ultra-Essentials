// VSCode MkDocs Screenshot Helper Extension
// This is a simplified version of a VSCode extension
// Save this as the main extension.js file

const vscode = require('vscode');
const fs = require('fs');
const path = require('path');
const { promisify } = require('util');
const writeFile = promisify(fs.writeFile);
const mkdir = promisify(fs.mkdir);
const stat = promisify(fs.stat);

// Helper function to generate a file name based on the current context
function generateFileName(document, format = 'png') {
    // Get the page name from the file name
    const pageName = path.basename(document.fileName, '.md').toLowerCase().replace(/\s+/g, '_');
    
    // Try to determine section from the content
    let sectionMatch = document.getText().match(/^#{2,3}\s+(.+)$/m);
    let sectionName = 'section';
    if (sectionMatch && sectionMatch[1]) {
        sectionName = sectionMatch[1].toLowerCase().replace(/[^a-z0-9]/g, '_').replace(/_+/g, '_').slice(0, 20);
    }
    
    // Add a timestamp-based unique identifier
    const timestamp = new Date().toISOString().replace(/[^0-9]/g, '').slice(0, 14);
    
    // Construct the filename
    return `${pageName}_${sectionName}_screenshot_v1.${format}`;
}

// Find the root of the MkDocs project
async function findMkDocsRoot(startPath) {
    let currentPath = startPath;
    
    // Keep going up the directory tree until we find mkdocs.yml or hit the root
    while (currentPath !== path.parse(currentPath).root) {
        const mkdocsPath = path.join(currentPath, 'mkdocs.yml');
        try {
            await stat(mkdocsPath);
            return currentPath; // Found the root
        } catch (e) {
            // Go up one directory
            currentPath = path.dirname(currentPath);
        }
    }
    
    // If we didn't find mkdocs.yml, return the starting directory as a fallback
    return startPath;
}

// Create the screenshot directory if it doesn't exist
async function ensureScreenshotDir(rootDir) {
    const screenshotDir = path.join(rootDir, 'docs', 'assets', 'screenshots');
    
    try {
        await stat(screenshotDir);
    } catch (e) {
        // Directory doesn't exist, create it
        await mkdir(screenshotDir, { recursive: true });
    }
    
    return screenshotDir;
}

// Handle pasted image data
async function handlePastedImage(imageData, editor) {
    try {
        // Get document and position
        const document = editor.document;
        const position = editor.selection.active;
        
        // Find MkDocs root
        const documentDir = path.dirname(document.fileName);
        const rootDir = await findMkDocsRoot(documentDir);
        
        // Ensure screenshot directory exists
        const screenshotDir = await ensureScreenshotDir(rootDir);
        
        // Generate filename
        const filename = generateFileName(document);
        const filePath = path.join(screenshotDir, filename);
        
        // Base64 data usually comes in format: data:image/png;base64,BASE64DATA
        const base64Data = imageData.split(',')[1];
        
        // Write the file
        await writeFile(filePath, Buffer.from(base64Data, 'base64'));
        
        // Get relative path for markdown
        const relativePath = path.relative(rootDir, filePath)
            .replace(/\\/g, '/') // Convert Windows backslashes to forward slashes
            .replace(/^docs\//, ''); // Remove docs/ prefix for MkDocs
        
        // Ask for alt text
        const altText = await vscode.window.showInputBox({
            prompt: 'Enter alt text for this image (for accessibility)',
            placeHolder: 'Describe what the screenshot shows'
        });
        
        // Format the markdown link
        let markdownLink;
        if (altText) {
            markdownLink = `![[${relativePath}|${altText}]]`;
        } else {
            markdownLink = `![[${relativePath}]]`;
        }
        
        // Insert the markdown link
        editor.edit(editBuilder => {
            editBuilder.insert(position, markdownLink);
        });
        
        // Show notification
        vscode.window.showInformationMessage(`Screenshot saved as ${filename}`);
        
    } catch (error) {
        vscode.window.showErrorMessage(`Error handling pasted image: ${error.message}`);
    }
}

// Activate the extension
function activate(context) {
    console.log('MkDocs Screenshot Helper extension is now active');
    
    // Register a command to handle pasted images
    const disposable = vscode.commands.registerCommand('mkdocs-screenshot.handlePaste', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            return;
        }
        
        try {
            // Read from clipboard
            const clipboard = await vscode.env.clipboard.readText();
            
            // Check if it's an image (base64 data)
            if (clipboard.startsWith('data:image/')) {
                await handlePastedImage(clipboard, editor);
            } else {
                // Not an image, just do a regular paste
                await vscode.commands.executeCommand('editor.action.clipboardPasteAction');
            }
        } catch (error) {
            vscode.window.showErrorMessage(`Error: ${error.message}`);
            // Fallback to regular paste
            await vscode.commands.executeCommand('editor.action.clipboardPasteAction');
        }
    });
    
    // Register a command to generate a screenshot filename
    const nameGenerator = vscode.commands.registerCommand('mkdocs-screenshot.generateName', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            return;
        }
        
        try {
            // Get document
            const document = editor.document;
            
            // Generate filename
            const filename = generateFileName(document);
            
            // Show the filename and allow copying
            const action = await vscode.window.showInformationMessage(
                `Generated filename: ${filename}`,
                'Copy to Clipboard'
            );
            
            if (action === 'Copy to Clipboard') {
                await vscode.env.clipboard.writeText(filename);
            }
        } catch (error) {
            vscode.window.showErrorMessage(`Error generating filename: ${error.message}`);
        }
    });
    
    // Register a custom handler for regular paste keyboard shortcut
    const pasteHandler = vscode.commands.registerCommand('editor.action.clipboardPasteAction', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor || editor.document.languageId !== 'markdown') {
            // Not in a markdown file, use regular paste
            await vscode.commands.executeCommand('default:editor.action.clipboardPasteAction');
            return;
        }
        
        try {
            // Check if clipboard contains image data
            const clipboard = await vscode.env.clipboard.readText();
            
            if (clipboard.startsWith('data:image/')) {
                // Contains image data, use our handler
                await handlePastedImage(clipboard, editor);
            } else {
                // Not an image, use regular paste
                await vscode.commands.executeCommand('default:editor.action.clipboardPasteAction');
            }
        } catch (error) {
            // Fallback to regular paste on error
            await vscode.commands.executeCommand('default:editor.action.clipboardPasteAction');
        }
    });
    
    // Add button to the editor toolbar
    const statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
    statusBarItem.text = "$(file-media) Screenshot Helper";
    statusBarItem.tooltip = "Generate a screenshot filename or handle pasted images";
    statusBarItem.command = 'mkdocs-screenshot.showMenu';
    statusBarItem.show();
    
    // Register the menu command
    const menuCommand = vscode.commands.registerCommand('mkdocs-screenshot.showMenu', async () => {
        const choice = await vscode.window.showQuickPick([
            { label: '$(file-media) Generate Screenshot Name', description: 'Create a name following conventions' },
            { label: '$(clippy) Paste Screenshot', description: 'Paste and process a screenshot from clipboard' }
        ]);
        
        if (choice) {
            if (choice.label.includes('Generate')) {
                await vscode.commands.executeCommand('mkdocs-screenshot.generateName');
            } else if (choice.label.includes('Paste')) {
                await vscode.commands.executeCommand('mkdocs-screenshot.handlePaste');
            }
        }
    });
    
    context.subscriptions.push(disposable, nameGenerator, pasteHandler, statusBarItem, menuCommand);
}

// Deactivate the extension
function deactivate() {}

module.exports = {
    activate,
    deactivate
};
