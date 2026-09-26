---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/filters
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_search_for_filters
title: "Jira v3 - Search for filters"
kind: request
request: "[[Jira v3 - Search for filters]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/filter/search · Search for filters. Returns a paginated list of filters. Use this operation to get: specific filters, by defining id only. filters that match all of the specified attributes. For example, all filters for a user with a particular word in their name. Writes data: no."
params:
  "filterName":
    type: string
    required: false
    description: "String used to perform a case-insensitive partial match with name."
  "accountId":
    type: string
    required: false
    description: "User account ID used to return filters with the matching owner.accountId. This parameter cannot be used with owner."
  "owner":
    type: string
    required: false
    description: "This parameter is deprecated because of privacy changes. Use accountId instead. See the migration guide for details. User name used to return filters with the matching owner.name."
  "groupname":
    type: string
    required: false
    description: "As a group's name can change, use of groupId is recommended to identify a group. Group name used to returns filters that are shared with a group that matches sharePermissions.group.groupname."
  "groupId":
    type: string
    required: false
    description: "Group ID used to returns filters that are shared with a group that matches sharePermissions.group.groupId. This parameter cannot be used with the groupname parameter."
  "projectId":
    type: string
    required: false
    description: "Project ID used to returns filters that are shared with a project that matches sharePermissions.project.id."
  "id":
    type: string
    required: false
    description: "The list of filter IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001. Do not exceed 200 filter IDs."
  "orderBy":
    type: string
    required: false
    description: "Order the results by a field: description Sorts by filter description. Note that this sorting works independently of whether the expand to display the description field is in use."
  "startAt":
    type: string
    required: false
    description: "The index of the first item to return in a page of results (page offset)."
  "maxResults":
    type: string
    required: false
    description: "The maximum number of items to return per page."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include: description Returns the description of the filter."
  "overrideSharePermissions":
    type: string
    required: false
    description: "EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be returned. Available to users with Administer Jira global permission."
  "isSubstringMatch":
    type: string
    required: false
    description: "When true this will perform a case-insensitive substring match for the provided filterName. When false the filter name will be searched using full text search syntax."
writes: false
expose: false
---
# jira_search_for_filters

`GET /rest/api/3/filter/search` — Search for filters

- Request: [[Jira v3 - Search for filters]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
