# Simple PowerShell script to serve the current folder as static HTTP server on port 8000

# The python module http.server uses the installed python; if you want to use a specific path, set $pythonPath
$pythonPath = "C:/Python314/python.exe"
$port = 8000
$cmd = "$pythonPath -m http.server $port"
Write-Host "Running: $cmd"
Invoke-Expression $cmd
