$exclude = @("venv", "Buscar_Livros.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Buscar_Livros.zip" -Force