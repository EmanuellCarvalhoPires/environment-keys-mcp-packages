---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/reports
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: PUT
path: "/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}"
category: "Reports"
writes_data: true
tool_note: "[[bitbucket_create_or_update_an_annotation]]"
---
# Bitbucket - Create or update an annotation

**Create or update an annotation** — `PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}`

- Run by the tool [[bitbucket_create_or_update_an_annotation]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
PUT {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/commit/{{param:commit}}/reports/{{param:reportId}}/annotations/{{param:annotationId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `repo_slug` (path, string, required) — The repository.
- `commit` (path, string, required) — The commit the report belongs to.
- `reportId` (path, string, required) — Either the uuid or external-id of the report.
- `annotationId` (path, string, required) — Either the uuid or external-id of the annotation.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates or updates an individual annotation for the specified report.
Annotations are individual findings that have been identified as part of a report, for example, a line of code that represents a vulnerability. These annotations can be attached to a specific file and even a specific line in that file, however, that is optional. Annotations are not mandatory and a report can contain up to 1000 annotations.

Just as reports, annotation needs to be uploaded with a unique ID that can later be used to identify the report as an alternative to the generated [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). If you want to use an existing id from your own system, we recommend prefixing it with your system's name to avoid collisions, for example, mySystem-annotation001.

### Sample cURL request:
```
curl --request PUT 'https://api.bitbucket.org/2.0/repositories///commit//reports/mySystem-001/annotations/mysystem-annotation001' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Security scan report",
    "annotation_type": "VULNERABILITY",
    "summary": "This line represents a security thread.",
    "severity": "HIGH",
    "path": "my-service/src/main/java/com/myCompany/mysystem/logic/Main.java",
    "line": 42
}'
```

### Possible field values:
annotation_type: VULNERABILITY, CODE_SMELL, BUG
result: PASSED, FAILED, IGNORED, SKIPPED
severity: HIGH, MEDIUM, LOW, CRITICAL

Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-insights-994316785.html) for more information.
