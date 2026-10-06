# Claude installation

## Claude app

Download `product-release-doc-writer.zip` without extracting it. Enable Code execution and file creation in Settings → Capabilities if needed. Open Customize → Skills, choose **+ Create skill**, then **Upload a skill**, and upload the ZIP. Enable the skill and start a fresh conversation with your document request and source material. These are the documented custom-skill controls; availability may depend on account or organization settings. [Official Claude guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Claude Code and Claude CLI

Claude Code's terminal command is `claude`; it uses the same skill installation rather than a separate CLI package. Extract the portable ZIP. Copy its `product-release-doc-writer` folder to either:

- Personal: `~/.claude/skills/product-release-doc-writer/`
- Project: `<your-project>/.claude/skills/product-release-doc-writer/`

Keep `SKILL.md`, `references/` and `assets/` together. Start Claude Code in the relevant local project and invoke `/product-release-doc-writer` with your request. Avoid installing duplicate copies at different scopes unless intentional. [Official Claude Code guide](https://code.claude.com/docs/en/skills).

Cloud and Cowork sessions do not use local personal folders in the same way; use an enabled account skill when those environments require it. For a desktop Code session, verify the skill is visible in that session before drafting. App loading and triggering remain runtime checks for the user.
