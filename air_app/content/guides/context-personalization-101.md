# Optimize Your Dev Setup For Evals w/ Cursor Rules & MCP

This is a guide to help you optimize your dev setup to get the most out of AI. It's showed with specific examples for eval frameworks, but the concepts are universally applicable to any tool. It's a guide to help you understand the different layers of context and how to use them to your advantage for your AI tools.

This content was originally created and taught as part of Hamel and Shreya's [AI Evals Course](https://maven.com/parlance-labs/evals?promoCode=kentro-learn) on Maven (30% off with that link!). If you are building AI tools or products, it's a must-take course. Watch the original video [here](https://maven.com/p/f24547/optimize-your-dev-setup-for-evals-w-cursor-rules-mcp).

[![Course Card](/static/CourseCard.jpg)](https://maven.com/kentro/context-engineering-for-coding?promoCode=ISAAC)

[**Enroll Now on Maven →**](https://maven.com/kentro/context-engineering-for-coding?promoCode=ISAAC)

## Why bother?

- Better AI assistance 
- Training cutoff may mean outdated info
- Spending time determining what's important to your project is good - Forces you to understand your tools better
- Make AI better match your taste
- Show how AI integrates with your other tools, abstractions, or framework

## The Three Layers

1. **General Context**: Generic tool that works on almost anything
    - Repomix, GitMCP, etc.
2. **Curated Context**: Curated by an expert, such as the tool author
    - Library provided MCP, llms.txt, etc.
3. **Personalized Context**: Context that you can create that's unique to your project
    - Only you can make this and it's uniquely tailored to your taste and needs

## General Context

General context is a good starting point when exploring or unsure about a tool. It's generic and not optimized for specific needs. It's fast and easy to set up. It's useful for quick experimentation and exploration, but it's not the best for long-term use. Here's a few examples of general context tools.

> **Good For**
> - Good starting point when exploring or unsure about a tool
> - Generic and not optimized for specific needs
> - Fast and easy to set up
> - Useful for quick experimentation and exploration

### Examples of General Context Tools

Here are examples of general context tools for different evaluation frameworks:

#### Braintrust - Repo Mix

RepoMix is a tool that lets you take a github repo and concatenate all the files based on a pattern into a single file. This is useful for getting lots of context into a single file that you model can easily understand.

![Repo Mix UI for Braintrust](/static/guides/braintrust/general/repomix_ui.png)

#### Phoenix - Paste Max

PasteMax is a tool that is a Native App you can install on your machine that lets you concatenate content and files directly in a nice UI. It serves a similar purpose to RepoMix, but it's a desktop app and has a different UX that many prefer.

![PasteMax UI for Phoenix](/static/guides/pheonix/general/PasteMax.png)
![PasteMax Ignores UI options](/static/guides/pheonix/general/PasteMaxIgnores.png)

#### Inspect - Git MCP

GitMCP is a tool that lets you use a github repo as a context source by creating an MCP server to let agents interact with the repo via tools. It's a different approach to general context, and it's a good way to be able to let agents interact with the repo via tools. It also has a nice web chat interface that's great for quick questions to explore the repo.

![GitMCP UI](/static/guides/inspect/general/mcp.png)

- Repository chat interface: https://gitmcp.io/UKGovernmentBEIS/inspect_evals/chat

![Chat interface](/static/guides/inspect/general/chat.png)

![MCP interface](/static/guides/inspect/general/mcp.png)

## Cursor Rules

Cursor rules let you customize how the cursor AI assistance will use your rules, this is extremely helpful and should not be overlooked.

### Rule Creation

You can create rules in the `.cursor/rules` directory, but there's a cursor command that does it for you.

![Cursor Rule Creation](/static/guides/cursor/rule_creation.png)

### Choosing a Rule Type

Cursor lets you choose a rule type to determine when the models will use the rule context. This is a great way to give a bit more control over model context.

![Cursor Rule Types](/static/guides/cursor/rule_types.png)

> **Rule Application Strategies**
>
> 1. **Always Apply** - Core rules that should never be violated
> 2. **Apply Manually** - Rules you trigger when needed. If you're really bad at thinking about context, and you're not going to put a lot of effort in then don't use this.
> 3. **Apply Intelligently** - This is a great thing to use
> 4. **Apply to Specific Files** - File-type or path-specific rules. This can be nice, but you're liable to set it to a path, restructure something, then forget and this rule will be accidentally deprecated.

## Curated Context

Curated context is a good starting point when you want to explore more deeply. It's provided by the tool author in some format and it's a good way to get a lot of context into a single file that you model can easily understand. This will usually be better than general context, but still not a very tiny investment to set up. However, not every tool or library provides curated context.

> **Good For**
> - You want to explore more deeply
> - It's provided by the tool author in some format

### Examples of Curated Context

Different tools provide curated context in various formats. Here are examples for different evaluation frameworks:

#### Braintrust - MCP (Model Context Protocol)

Braintrust provides a MCP server that your AI agents can use. This is a lot like GitMCP we saw above, but created by the Braintrust team specifically for Braintrust so it's much better.

- Official MCP server: [https://www.braintrust.dev/docs/reference/mcp](https://www.braintrust.dev/docs/reference/mcp)
- Provides structured access to Braintrust functionality

To set up the MCP server with Cursor, you can use the following settings.

![Cursor MCP Settings](/static/guides/braintrust/curated/CursorMCPSettings.png)

![Cursor MCP Json](/static/guides/braintrust/curated/CursorMCPJson.png)

#### Phoenix - LLMs.txt

Phoenix provides an file based in the [llms.txt spec](https://llmstxt.org/) format. This is a format that allows for use as static context in a flat file, or as a tool that an MCP server can use to crawl it agentally.

- Standard Format for Phoenix: [https://arize.com/docs/phoenix/llms.txt](https://arize.com/docs/phoenix/llms.txt)
- Langchain MCP documentation tool: [https://github.com/langchain-ai/mcpdoc](https://github.com/langchain-ai/mcpdoc)

#### Inspect - llms.txt

For Phoenix, I provided a link to langchain's MCP server that lets you use the llms.txt file as a tool. For Inspect, let's use the llms.txt spec to use the flat files as context to see the difference.

- Standard format: [https://inspect.aisi.org.uk/llms.txt](https://inspect.aisi.org.uk/llms.txt)
- Full version: [https://inspect.aisi.org.uk/llms-full.txt](https://inspect.aisi.org.uk/llms-full.txt)
- Individual Pages as Context: [https://inspect.aisi.org.uk/index.html.md](https://inspect.aisi.org.uk/index.html.md)

### Manual Approaches

Manual curation of context is also a great way to have the most control. There is typically a tradeoff between the amount of time you spend curating the context and the quality of the context. You will get better results if you spend more time carefully curating the context, and whether that payoff is worth the time is dependent on a few things:

1. How long will you be using this tool and how much? If you use it daily and will for years, it's worth the time to curate the context.
2. How good is the library provided context? If they have carefully curated the context for llms specifically and the tool authors use it themselves, the often it works pretty great out of the box. Sadly, most tools don't do this (yet).

#### Jina AI

Jina AI is an easy way to turn any html page into a markdown file. Markdown is much better context for HTML, because there's loads of unnecessary noise in the HTML that doesn't add value (styling classes, js interactivity, server calls, social media icons, etc.)

![Jina AI](/static/guides/inspect/curated/JinaAI.png)

#### Copy Outer HTML

By going more manual you can remove the noise and get a more focused context. This is a great way to get a more focused context, but it's a more work. The main benefits here over Jina AI is you often can remove lots of unneeded sections like footers, table of contents, sidebars, navigation, etc.

Copying the outer HTML and feeding that into Web2Md is the best workflow I've found for this.

![Copy Outer HTML](/static/guides/inspect/curated/CopyOuterHTML.png)

#### Web 2 MD

![Web 2 MD](/static/guides/inspect/curated/Web2Md.png)

## Personalized Context

Personalized context is the most time consuming and the most effective. It's not something anyone can create for you because it matches your taste and decisions made for you specific project.

> **Good For**
> - You know you're going to be using this thing for months
> - It's worthwhile to invest a bit of time for better AI assistance

Let's look at some examples of diffs that you may want to do to your context for more personalized context.

### Examples of Personalized Context

Here are examples of how to personalize context for different evaluation frameworks:

#### Braintrust Personalization Examples

**Use Case Specific Context**

![Use case specific examples](/static/guides/braintrust/personalized/UseCase.png)

**Reducing Context Size**

![Reducing context for efficiency](/static/guides/braintrust/personalized/ReduceContext.png)

**Opinionated Best Practices**

![Defining coding standards](/static/guides/braintrust/personalized/Opinionated.png)

**Multi-Language Support**

![Supporting multiple languages](/static/guides/braintrust/personalized/MultiLang.png)

**Code Style Preferences**

![Insert your coding style](/static/guides/braintrust/personalized/CodeInsertYourStyle.png)

**Performance Considerations**

![Removing timing-specific code](/static/guides/braintrust/personalized/CodeRmTiming.png)

#### Phoenix Personalization Examples

**Fix Formatting**

![Fix Formatting](/static/guides/pheonix/personalized/FormattingFix.png)

**Remove hosted options you're not using**

![Remove Cloud Hosting](/static/guides/pheonix/personalized/RmCloudHosted.png)

**Put in project specific info**

![Put in Real Endpoints](/static/guides/pheonix/personalized/RmCopyPutInRealInfo.png)

**Remove Unused Languages**

![Remove Typescript](/static/guides/pheonix/personalized/TypeScript.png)

#### Inspect Personalization Examples

**Human prose → AI Instruction**

![Change tip to instruction for env var clarity](/static/guides/inspect/personalized/EnvVariableClarity.png)

**Remove examples not relevant to you**

![Remove non-relevant examples](/static/guides/inspect/personalized/TrimExamples.png)