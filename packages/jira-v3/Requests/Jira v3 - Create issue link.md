---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-links
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issueLink"
category: "Issue links"
writes_data: true
tool_note: "[[jira_create_issue_link]]"
---
# Jira v3 - Create issue link

**Create issue link** — `POST /rest/api/3/issueLink`

- Run by the tool [[jira_create_issue_link]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issueLink
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "comment": {
    "body": {
      "content": [
        {
          "content": [
            {
              "text": "Linked related issue!",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "visibility": {
      "identifier": "276f955c-63d7-42c8-9520-92d01dca0625",
      "type": "group",
      "value": "jira-software-users"
    }
  },
  "inwardIssue": {
    "key": "HSP-1"
  },
  "outwardIssue": {
    "key": "MKY-1"
  },
  "type": {
    "name": "Duplicate"
  }
}
```

## Original description

Creates a link between two issues. Use this operation to indicate a relationship between two issues and optionally add a comment to the from (outward) issue. To use this resource the site must have [Issue Linking](https://confluence.atlassian.com/x/yoXKM) enabled.

This resource returns nothing on the creation of an issue link. To obtain the ID of the issue link, use `https://your-domain.atlassian.net/rest/api/3/issue/[linked issue key]?fields=issuelinks`.

If the link request duplicates a link, the response indicates that the issue link was created. If the request included a comment, the comment is added.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the issues to be linked,
 *  *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) on the project containing the from (outward) issue,
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.
