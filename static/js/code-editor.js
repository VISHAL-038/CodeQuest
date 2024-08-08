var editor = CodeMirror(document.getElementById('code-editor'), {
    mode: 'python',
    lineNumbers: true,
    theme: 'monokai'
});

function runCode() {
    var code = editor.getValue();
    try {
        var output = eval(code);
        document.getElementById('output').textContent = 'Output:\n' + output;
    } catch (e) {
        document.getElementById('output').textContent = 'Error:\n' + e.message;
    }
}


  





