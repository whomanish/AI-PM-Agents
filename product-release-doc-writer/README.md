# Product Release Doc Writer

A provider-neutral Agent Skill for creating or revising five product-release documents from the context you supply.

| Document | Purpose |
|---|---|
| Internal Release Notes | Align teams on rollout, risks, dependencies, decisions and actions. |
| External Release Notes | Explain customer value, availability and verified usage. |
| Product Release Plan | Plan execution around learning, validation and rollout evidence. |
| Feature FAQ | Answer questions about capability, access, usage and limits. |
| Support FAQ | Separate expected behavior, access issues, limitations, defects and verified guidance. |

## Download and install

| Environment | Download or source | Instructions |
|---|---|---|
| Claude app | [Portable skill ZIP](https://github.com/whomanish/AI-PM-Agents/releases/download/product-release-doc-writer-v0.1.0/product-release-doc-writer.zip) | [Claude installation](docs/claude-install.md) |
| Claude Code, including the `claude` CLI | Portable skill ZIP | [Claude installation](docs/claude-install.md) |
| Codex app and Codex CLI | Portable skill ZIP | [Codex installation](docs/openai-install.md#codex-app-and-cli) |
| ChatGPT with plugin support | [OpenAI plugin ZIP](https://github.com/whomanish/AI-PM-Agents/releases/download/product-release-doc-writer-v0.1.0/product-release-doc-writer-openai-plugin.zip), or this source folder | [ChatGPT installation](docs/openai-install.md#chatgpt) |

Download the ZIPs from the [product-release-doc-writer-v0.1.0 release](https://github.com/whomanish/AI-PM-Agents/releases/tag/product-release-doc-writer-v0.1.0). Extract the portable ZIP for local folder installation; upload it intact in Claude's skill settings.

Both downloads contain identical skill instructions, reference guides and templates. The OpenAI download adds plugin metadata; the portable download includes a content manifest. Neither needs an API key or a connected service. Host application features and permissions determine which installation route is available. Installation instructions were checked against official documentation on 6 October 2026; loading and triggering in every app have not been verified here.

## Use

Select or invoke the installed skill, then specify the document and audience. Supply the feature facts, release status, verified steps, constraints, owners and dates you actually know. Label which facts are public and which are internal. You may also provide a preferred template and separate style examples.

Example request:

> Use Product Release Doc Writer to draft external release notes from the attached approved public brief. Follow the attached release-note template. Keep internal planning information out of the customer-facing document.

For internal documents, request Internal Release Notes, a Product Release Plan or a Support FAQ and supply the relevant internal context. For revisions, attach the existing document and describe the change.

The skill supports evidence-based drafting, flags material conflicts and labels proposed actions. Review the generated document before using or publishing it.

## Customize and rebuild

See [customization](docs/customization.md). The canonical skill is under `skills/product-release-doc-writer/`; `plugin.json` and the repository-root `.agents/plugins/marketplace.json` provide the OpenAI wrapper and local discovery metadata.

To rebuild both downloads with Python 3:

Run this from the `product-release-doc-writer/` directory:

```sh
python3 scripts/package.py
```

Checksums and member manifests accompany the ZIPs as release assets. Local rebuilds write them to `downloads/`. Rebuilding does not publish anything.

## Privacy and support

See [privacy information](docs/privacy.md) for the instruction-only package's data practices, and [support](docs/support.md) to report installation problems or package defects.

## License

MIT. Copyright 2026 Manish Jha. See [LICENSE](LICENSE).
