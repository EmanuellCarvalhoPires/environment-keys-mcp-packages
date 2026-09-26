---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_projects_paginated
title: "Jira v3 - Get projects paginated"
kind: request
request: "[[Jira v3 - Get projects paginated]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/project/search · Get projects paginated. Returns a paginated list of projects visible to the user. This operation can be accessed anonymously. Permissions required: Projects are returned only where the user has one of: Browse Projects project permission for the project. Writes data: no."
params:
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page. Must be less than or equal to 100. If a value greater than 100 is provided, the maxResults parameter will default to 100."
  "orderBy":
    type: string
    required: false
    description: "Order the results by a field. category Sorts by project category. A complete list of category IDs is found using Get all project categories."
  "id":
    type: string
    required: false
    description: "The project IDs to filter the results by. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001. Up to 50 project IDs can be provided."
  "keys":
    type: string
    required: false
    description: "The project keys to filter the results by. To include multiple keys, provide an ampersand-separated list. For example, keys=PA&keys=PB. Up to 50 project keys can be provided."
  "query":
    type: string
    required: false
    description: "Filter the results using a literal string. Projects with a matching key or name are returned (case insensitive)."
  "typeKey":
    type: string
    required: false
    description: "Orders results by the project type. This parameter accepts a comma-separated list. Valid values are business, servicedesk, and software."
  "categoryId":
    type: string
    required: false
    description: "The ID of the project's category. A complete list of category IDs is found using the Get all project categories operation."
  "action":
    type: string
    required: false
    description: "Filter results by projects for which the user can: view the project, meaning that they have one of the following permissions: Browse projects project permission for the project."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include: description Returns the project description."
  "status":
    type: string
    required: false
    description: "EXPERIMENTAL. Filter results by project status: live Search live projects. archived Search archived projects. deleted Search deleted projects, those in the recycle bin."
  "properties":
    type: string
    required: false
    description: "EXPERIMENTAL. A list of project properties to return for the project. This parameter accepts a comma-separated list."
  "propertyQuery":
    type: string
    required: false
    description: "EXPERIMENTAL. A query string used to search properties. The query string cannot be specified using a JSON object."
writes: false
expose: true
---
# jira_get_projects_paginated

`GET /rest/api/3/project/search` — Get projects paginated

- Request: [[Jira v3 - Get projects paginated]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
