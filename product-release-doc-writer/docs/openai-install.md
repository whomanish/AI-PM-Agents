# OpenAI installation

## Codex app and CLI

Extract `product-release-doc-writer.zip`. Copy the enclosed folder to `~/.agents/skills/product-release-doc-writer/` for personal use, or `<your-project>/.agents/skills/product-release-doc-writer/` for project use. Keep its references and templates together. Start a fresh Codex session in that project and explicitly request `$product-release-doc-writer` with your document task. If it is missing, restart Codex. [Official skill documentation](https://learn.chatgpt.com/docs/build-skills).

## ChatGPT

Use the OpenAI plugin package when your ChatGPT environment supports plugins. For desktop local installation, download this repository's complete source folder, including hidden `.agents/` files. Open it as a local project. Its `.agents/plugins/marketplace.json` points to `product-release-doc-writer/`. Restart the desktop app and check that the plugin appears; select/install it through the available plugin controls. [Official local plugin packaging instructions](https://developers.openai.com/plugins/build/plugins).

To use the plugin from another local project, extract `product-release-doc-writer-openai-plugin.zip` to that project's `plugins/product-release-doc-writer/`. Add the following entry to that project's `.agents/plugins/marketplace.json`, preserving any existing entries:

```json
{
  "name": "product-release-doc-writer",
  "source": {"source": "local", "path": "./plugins/product-release-doc-writer"},
  "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
  "category": "Productivity"
}
```

The entry belongs in the marketplace's `plugins` array. The complete marketplace in this repository can serve as a starting point. This skill-only plugin has no service authentication.

Once installed, start a conversation, type `@`, select the plugin under Plugins and supply your task and sources. Plugin use requires the relevant workspace permissions. [Official ChatGPT plugin guide](https://learn.chatgpt.com/docs/build-plugins).

A GitHub download is separate from installation in ChatGPT web/mobile or a managed workspace. A public Plugins Directory listing requires separate submission and approval; no listing is claimed here. Do not treat attaching either ZIP to a normal chat as native installation. If local plugins are unavailable, the downloadable wrapper alone cannot enable that feature. [Official publication route](https://developers.openai.com/plugins/deploy/submission).

Use either the standalone skill or the plugin in a session to avoid duplicate copies. These are documentation-backed routes; runtime loading and triggering have not been verified here.
