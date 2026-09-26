---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-types
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issuetype/{id}/avatar2"
category: "Issue types"
writes_data: true
tool_note: "[[jira_load_issue_type_avatar]]"
---
# Jira v3 - Load issue type avatar

**Load issue type avatar** — `POST /rest/api/3/issuetype/{id}/avatar2`

- Run by the tool [[jira_load_issue_type_avatar]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issuetype/{{param:id}}/avatar2?x={{param:x}}&y={{param:y}}&size={{param:size}}
Authorization: {{service.auth_token}}
Content-Type: */*

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the issue type.
- `x` (query, string, optional) — The X coordinate of the top-left corner of the crop region.
- `y` (query, string, optional) — The Y coordinate of the top-left corner of the crop region.
- `size` (query, string, required) — The length of each side of the crop region.
- `body` (body, string, required) — Request body (*/*).

## Original description

Loads an avatar for the issue type.

Specify the avatar's local file location in the body of the request. Also, include the following headers:

 *  `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more information see [Special Headers](#special-request-headers).
 *  `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.

For example:  
`curl --request POST \ --user email@example.com: \ --header 'X-Atlassian-Token: no-check' \ --header 'Content-Type: image/' \ --data-binary "" \ --url 'https://your-domain.atlassian.net/rest/api/3/issuetype/{issueTypeId}'This`

The avatar is cropped to a square. If no crop parameters are specified, the square originates at the top left of the image. The length of the square's sides is set to the smaller of the height or width of the image.

The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.

After creating the avatar, use [ Update issue type](#api-rest-api-3-issuetype-id-put) to set it as the issue type's displayed avatar.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
