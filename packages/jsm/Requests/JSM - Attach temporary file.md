---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/action
  - api/effect/write
  - api/format/multipart
up: "[[MCP - JSM]]"
app: "JSM"
method: POST
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/attachTemporaryFile"
category: "Servicedesk"
writes_data: true
---
# JSM - Attach temporary file

**Attach temporary file** — `POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/attachTemporaryFile`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM - Attach temporary file"`.
- **Format:** the endpoint expects `multipart/form-data` (file upload), which the plugin `http` block cannot build. Kept as reference.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/attachTemporaryFile
Authorization: {{service.auth_token}}
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the Service Desk to which the file will be attached. This can alternatively be a project identifier.

## Original description

This method adds one or more temporary attachments to a service desk, which can then be permanently attached to a customer request using [servicedeskapi/request/\{issueIdOrKey\}/attachment](#api-request-issueIdOrKey-attachment-post).

**Note**: It is possible for a service desk administrator to turn off the ability to add attachments to a service desk.

This method expects a multipart request. The media-type multipart/form-data is defined in RFC 1867. Most client libraries have classes that make dealing with multipart posts simple. For instance, in Java the Apache HTTP Components library provides [MultiPartEntity](http://hc.apache.org/httpcomponents-client-ga/httpmime/apidocs/org/apache/http/entity/mime/MultipartEntity.html).

Because this method accepts multipart/form-data, it has XSRF protection on it. This means you must submit a header of X-Atlassian-Token: no-check with the request or it will be blocked.

The name of the multipart/form-data parameter that contains the attachments must be `file`.

For example, to upload a file called `myfile.txt` in the Service Desk with ID 10001 use

    curl -D- -u customer:customer -X POST -H "X-ExperimentalApi: opt-in" -H "X-Atlassian-Token: no-check" -F "file=@myfile.txt" https://your-domain.atlassian.net/rest/servicedeskapi/servicedesk/10001/attachTemporaryFile

**[Permissions](#permissions) required**: Permission to add attachments in this Service Desk.
