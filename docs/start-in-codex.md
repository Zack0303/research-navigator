# Start in Codex / 在 Codex 中开始 / Empezar en Codex
Documentation checked: 2026-10-16. Menu labels may vary by app version. This guide is documentation-backed; the desktop clicks have not been exercised in this project.

## 1. Connect the folder / 连接文件夹 / Conecta la carpeta
Use a local project. In its menu, choose **Edit project → Add folder** and select the extracted repository folder containing SKILL.md. Make it primary if you want new chats to start there. Start a chat in that project.

中文：在本地项目菜单选择 Edit project → Add folder，选择包含 SKILL.md 的仓库文件夹。需要让新对话从这里开始时，将其设为主文件夹。然后在项目内开始对话。

Español: en un proyecto local, selecciona Edit project → Add folder y elige la carpeta que contiene SKILL.md. Hazla principal si quieres iniciar allí los nuevos chats. Abre un chat dentro del proyecto.

Source: [Official project documentation](https://learn.chatgpt.com/docs/projects), “Use local projects for folders and codebases”. A ChatGPT project with uploaded sources is different from a local-folder project.

## 2. Check access / 确认能读文件 / Comprueba el acceso
Paste:
```text
Find and read SKILL.md in the research-navigator folder attached to this project. Tell me its name and check that references/source-verification.md is readable. If you cannot find them, say what is missing; do not pretend to load the Skill.
```
Expected: research-navigator, and confirmation based on actual reads. If not found, check that the selected folder contains SKILL.md directly; it may be inside another extracted folder. Keep the whole repository together. Do not troubleshoot by uploading private research.

## 3. Try a task / 开始体验 / Prueba una tarea
Copy the idea-only prompt from your [English](../README.md), [中文](../README.zh-CN.md) or [Español](../README.es.md) README. No Python or API key is needed for planning/review through this route. Your existing agent access and usage limits apply.

Look for a provisional direction, a few questions, unknown requirements and a next action. If the agent invents rules, ask it for the exact official source and applicability; unverified rules should stay unknown.

## Optional automatic discovery
The repository-root SKILL.md is explicitly read by the prompts above. It is not automatically discovered solely because it sits at the root. Official Codex local discovery uses `.agents/skills` directories; the installer can also download repository skills. See [official Skill documentation](https://learn.chatgpt.com/docs/build-skills), “Where Codex loads local skills” and “Install curated skills for local use”. This project has not validated an automatic-install route, so explicit reading remains the recommended first trial.

## When capabilities are missing
No browsing: provisional planning is still possible; current university/scholar evidence cannot be verified. No file writing: discuss a scholar profile, but do not promise a saved bundle. A folder-access confirmation is not a guarantee that later reasoning is correct.
