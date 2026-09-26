---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-avatars
  - api/operation/action
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/project/{projectIdOrKey}/avatar2"
category: "Project avatars"
writes_data: true
tool_note: "[[jira_load_project_avatar]]"
---
# Jira v3 - Load project avatar

**Load project avatar** — `POST /rest/api/3/project/{projectIdOrKey}/avatar2`

- Run by the tool [[jira_load_project_avatar]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/avatar2?x={{param:x}}&y={{param:y}}&size={{param:size}}
Authorization: {{service.auth_token}}
Content-Type: */*

{{param:body}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The ID or (case-sensitive) key of the project.
- `x` (query, string, optional) — The X coordinate of the top-left corner of the crop region.
- `y` (query, string, optional) — The Y coordinate of the top-left corner of the crop region.
- `size` (query, string, optional) — The length of each side of the crop region.
- `body` (body, string, required) — Request body (*/*).

## Original description

Loads an avatar for a project.

Specify the avatar's local file location in the body of the request. Also, include the following headers:

 *  `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more information see [Special Headers](#special-request-headers).
 *  `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.

For example:  
`curl --request POST `

`--user email@example.com: `

`--header 'X-Atlassian-Token: no-check' `

`--header 'Content-Type: image/' `

`--data-binary "" `

`--url 'https://your-domain.atlassian.net/rest/api/3/project/{projectIdOrKey}/avatar2'`

The avatar is cropped to a square. If no crop parameters are specified, the square originates at the top left of the image. The length of the square's sides is set to the smaller of the height or width of the image.

The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.

After creating the avatar use [Set project avatar](#api-rest-api-3-project-projectIdOrKey-avatar-put) to set it as the project's displayed avatar.

**[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
