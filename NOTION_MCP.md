# Notion MCP

Se utiliza el servidor oficial remoto de Notion con OAuth. No requiere instalar paquetes npm ni guardar un token de integración.

## Codex (aplicación, CLI y extensión)

La configuración de usuario se encuentra en `C:\Users\herna\.codex\config.toml`:

```toml
[mcp_servers.notion]
url = "https://mcp.notion.com/mcp"
```

Para registrarlo en otra instalación y autorizar el acceso:

```powershell
codex mcp add notion --url https://mcp.notion.com/mcp
codex mcp login notion
codex mcp list
```

Completa la autorización en Notion y abre una nueva sesión de Codex para cargar sus herramientas.

## VS Code / GitHub Copilot

El proyecto incluye `.vscode/mcp.json`. Abre la paleta con `Ctrl+Shift+P`, ejecuta `MCP: List Servers`, selecciona `notion` e inicia el servidor. Completa la autorización OAuth cuando se solicite. Esta configuración es independiente de la extensión de Codex; cada cliente puede solicitar su propia autorización.

## Comprobar acceso

Primero pide: «Busca mi tablero Proyecto de Título en Notion y muestra sus propiedades, sin modificarlo».

Después puedes pedir: «Crea una tarea Implementar login en ese tablero, con prioridad Alta y estado Por hacer». Los nombres de propiedades y opciones deben coincidir con los de tu tablero.

Si no aparece el tablero, verifica la cuenta, el workspace y los permisos de acceso en Notion.

Revoca el token de integración compartido en el chat desde la configuración de integraciones de Notion. Esta conexión OAuth no lo necesita.

## Fuentes

- https://developers.notion.com/guides/mcp/get-started-with-mcp
- https://developers.openai.com/codex/mcp
