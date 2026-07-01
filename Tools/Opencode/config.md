### Opencode config space

This is because not all projects have the same rules/structure, and sometimes you will find yourself working with teams.

- **Global Config**: to be found/placed in (~/.config/opencode/opencode.json), these are the user's preference.
- **Project config**: (opencode.json) in a project dir, contains project-specific settings.
- **.opencode directories**: contains (agents, commands, plugins)
- **Custom overrides:** (OPENCODE_CONFIG) env var
- **Runtime overrides:** (OPENCODE_CONFIG_CONTENT) env var

[Visit the DOCS](https://opencode.ai/docs/config/) for an in-depth explanation with examples.
