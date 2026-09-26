---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/members/{id}"
category: "Members"
writes_data: true
---
# Trello - Update a Member

**Update a Member** — `PUT /members/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/members/{{param:id}}?fullName={{param:fullName}}&initials={{param:initials}}&username={{param:username}}&bio={{param:bio}}&avatarSource={{param:avatarSource}}&prefs/colorBlind={{param:prefs_colorBlind}}&prefs/locale={{param:prefs_locale}}&prefs/minutesBetweenSummaries={{param:prefs_minutesBetweenSummaries}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `fullName` (query, string, optional) — New name for the member. Cannot begin or end with a space.
- `initials` (query, string, optional) — New initials for the member. 1-4 characters long.
- `username` (query, string, optional) — New username for the member. At least 3 characters long, only lowercase letters, underscores, and numbers. Must be unique.
- `bio` (query, string, optional) — Query parameter bio.
- `avatarSource` (query, string, optional) — One of: gravatar, none, upload
- `prefs_colorBlind` (query, string, optional) — Query parameter prefs/colorBlind.
- `prefs_locale` (query, string, optional) — Query parameter prefs/locale.
- `prefs_minutesBetweenSummaries` (query, string, optional) — -1 for disabled, 1, or 60

## Original description

Update a Member
