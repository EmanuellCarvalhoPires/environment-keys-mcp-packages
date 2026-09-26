---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_search_for_dashboards
title: "Jira v3 - Search for dashboards"
kind: request
request: "[[Jira v3 - Search for dashboards]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/dashboard/search · Search for dashboards. Returns a paginated list of dashboards. This operation is similar to Get dashboards except that the results can be refined to include dashboards that have specific attributes. For example, dashboards with a particular name. Writes data: no."
params:
  "dashboardName":
    type: string
    required: false
    description: "String used to perform a case-insensitive partial match with name."
  "accountId":
    type: string
    required: false
    description: "User account ID used to return dashboards with the matching owner.accountId. This parameter cannot be used with the owner parameter."
  "owner":
    type: string
    required: false
    description: "This parameter is deprecated because of privacy changes. Use accountId instead. See the migration guide for details. User name used to return dashboards with the matching owner.name."
  "groupname":
    type: string
    required: false
    description: "As a group's name can change, use of groupId is recommended. Group name used to return dashboards that are shared with a group that matches sharePermissions.group.name."
  "groupId":
    type: string
    required: false
    description: "Group ID used to return dashboards that are shared with a group that matches sharePermissions.group.groupId. This parameter cannot be used with the groupname parameter."
  "projectId":
    type: string
    required: false
    description: "Project ID used to returns dashboards that are shared with a project that matches sharePermissions.project.id."
  "orderBy":
    type: string
    required: false
    description: "Order the results by a field: description Sorts by dashboard description. Note that this sort works independently of whether the expand to display the description field is in use."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "status":
    type: string
    required: false
    description: "The status to filter by. It may be active, archived or deleted."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about dashboard in the response. This parameter accepts a comma-separated list."
writes: false
expose: false
---
# jira_search_for_dashboards

`GET /rest/api/3/dashboard/search` — Search for dashboards

- Request: [[Jira v3 - Search for dashboards]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
