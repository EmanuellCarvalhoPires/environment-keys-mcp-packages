---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/app-migration
  - api/operation/update
  - api/effect/write
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/atlassian-connect/1/migration/field"
category: "App migration"
writes_data: true
---
# Jira v3 - Bulk update custom field value

**Bulk update custom field value** — `PUT /rest/atlassian-connect/1/migration/field`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Bulk update custom field value"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/atlassian-connect/1/migration/field
Authorization: {{service.auth_token}}
Accept: application/json
Atlassian-Transfer-Id: {{param:atlassian_transfer_id}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `atlassian_transfer_id` (header, string, required) — Value of the `Atlassian-Transfer-Id` header.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "updateValueList": [
    {
      "_type": "StringIssueField",
      "issueID": 10001,
      "fieldID": 10076,
      "string": "new string value"
    },
    {
      "_type": "TextIssueField",
      "issueID": 10002,
      "fieldID": 10077,
      "text": "new text value"
    },
    {
      "_type": "SingleSelectIssueField",
      "issueID": 10003,
      "fieldID": 10078,
      "optionID": "1"
    },
    {
      "_type": "MultiSelectIssueField",
      "issueID": 10004,
      "fieldID": 10079,
      "optionID": "2"
    },
    {
      "_type": "RichTextIssueField",
      "issueID": 10005,
      "fieldID": 10080,
      "richText": "new rich text value"
    },
    {
      "_type": "NumberIssueField",
      "issueID": 10006,
      "fieldID": 10082,
      "number": 54
    }
  ]
}
```

## Original description

Updates the value of a custom field added by Connect apps on one or more issues.
The values of up to 200 custom fields can be updated.

**[Permissions](#permissions) required:** Only Connect apps can make this request
