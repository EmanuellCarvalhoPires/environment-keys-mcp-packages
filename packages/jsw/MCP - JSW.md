---
tags:
  - moc
  - mcp
  - api/app/jira-software
up: "[[MCP Tools]]"
---
# MCP - JSW

- **Tools:** 61 (exposed: 4; the others via `run_vault_tool`)
- **Requests only:** 44
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/jira/software/rest/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Backlog

- [[jsw_move_issues_to_backlog]] — `POST /rest/agile/1.0/backlog/issue` — Move issues to backlog ✏️
- [[jsw_move_issues_to_backlog_for_board]] — `POST /rest/agile/1.0/backlog/{boardId}/issue` — Move issues to backlog for board ✏️

## Board

- [[jsw_get_all_boards]] — `GET /rest/agile/1.0/board` — Get all boards ⭐
- [[jsw_create_board]] — `POST /rest/agile/1.0/board` — Create board ✏️
- [[jsw_get_board_by_filter_id]] — `GET /rest/agile/1.0/board/filter/{filterId}` — Get board by filter id
- [[jsw_get_board]] — `GET /rest/agile/1.0/board/{boardId}` — Get board
- [[jsw_delete_board]] — `DELETE /rest/agile/1.0/board/{boardId}` — Delete board ✏️
- [[jsw_get_issues_for_backlog]] — `GET /rest/agile/1.0/board/{boardId}/backlog` — Get issues for backlog
- [[jsw_get_issues_for_backlog_enhanced]] — `GET /rest/software/1.0/board/{boardId}/backlog` — Get issues for backlog (enhanced)
- [[jsw_get_approximate_issue_count_for_backlog]] — `GET /rest/software/1.0/board/{boardId}/backlog/approximate-count` — Get approximate issue count for backlog
- [[jsw_get_configuration]] — `GET /rest/agile/1.0/board/{boardId}/configuration` — Get configuration
- [[jsw_get_epics]] — `GET /rest/agile/1.0/board/{boardId}/epic` — Get epics
- [[jsw_get_issues_without_epic_for_board]] — `GET /rest/agile/1.0/board/{boardId}/epic/none/issue` — Get issues without epic for board
- [[jsw_get_issues_without_epic_for_board_enhanced]] — `GET /rest/software/1.0/board/{boardId}/epic/none/issue` — Get issues without epic for board (enhanced)
- [[jsw_get_board_issues_for_epic]] — `GET /rest/agile/1.0/board/{boardId}/epic/{epicId}/issue` — Get board issues for epic
- [[jsw_get_board_issues_for_epic_enhanced]] — `GET /rest/software/1.0/board/{boardId}/epic/{epicId}/issue` — Get board issues for epic (enhanced)
- [[jsw_get_features_for_board]] — `GET /rest/agile/1.0/board/{boardId}/features` — Get features for board
- [[jsw_toggle_features]] — `PUT /rest/agile/1.0/board/{boardId}/features` — Toggle features ✏️
- [[jsw_get_issues_for_board]] — `GET /rest/agile/1.0/board/{boardId}/issue` — Get issues for board ⭐
- [[jsw_move_issues_to_board]] — `POST /rest/agile/1.0/board/{boardId}/issue` — Move issues to board ✏️
- [[jsw_get_issues_for_board_enhanced]] — `GET /rest/software/1.0/board/{boardId}/issue` — Get issues for board (enhanced)
- [[jsw_get_approximate_issue_count_for_board]] — `GET /rest/software/1.0/board/{boardId}/issue/approximate-count` — Get approximate issue count for board
- [[jsw_get_projects]] — `GET /rest/agile/1.0/board/{boardId}/project` — Get projects
- [[jsw_get_projects_full]] — `GET /rest/agile/1.0/board/{boardId}/project/full` — Get projects full
- [[jsw_get_board_property_keys]] — `GET /rest/agile/1.0/board/{boardId}/properties` — Get board property keys
- [[jsw_get_board_property]] — `GET /rest/agile/1.0/board/{boardId}/properties/{propertyKey}` — Get board property
- [[jsw_set_board_property]] — `PUT /rest/agile/1.0/board/{boardId}/properties/{propertyKey}` — Set board property ✏️
- [[jsw_delete_board_property]] — `DELETE /rest/agile/1.0/board/{boardId}/properties/{propertyKey}` — Delete board property ✏️
- [[jsw_get_all_quick_filters]] — `GET /rest/agile/1.0/board/{boardId}/quickfilter` — Get all quick filters
- [[jsw_get_quick_filter]] — `GET /rest/agile/1.0/board/{boardId}/quickfilter/{quickFilterId}` — Get quick filter
- [[jsw_get_reports_for_board]] — `GET /rest/agile/1.0/board/{boardId}/reports` — Get reports for board
- [[jsw_get_all_sprints]] — `GET /rest/agile/1.0/board/{boardId}/sprint` — Get all sprints ⭐
- [[jsw_get_board_issues_for_sprint]] — `GET /rest/agile/1.0/board/{boardId}/sprint/{sprintId}/issue` — Get board issues for sprint
- [[jsw_get_board_issues_for_sprint_enhanced]] — `GET /rest/software/1.0/board/{boardId}/sprint/{sprintId}/issue` — Get board issues for sprint (enhanced)
- [[jsw_get_all_versions]] — `GET /rest/agile/1.0/board/{boardId}/version` — Get all versions

## Epic

- [[jsw_get_issues_without_epic]] — `GET /rest/agile/1.0/epic/none/issue` — Get issues without epic
- [[jsw_remove_issues_from_epic]] — `POST /rest/agile/1.0/epic/none/issue` — Remove issues from epic ✏️
- [[jsw_get_issues_without_epic_enhanced]] — `GET /rest/software/1.0/epic/none/issue` — Get issues without epic (enhanced)
- [[jsw_get_epic]] — `GET /rest/agile/1.0/epic/{epicIdOrKey}` — Get epic
- [[jsw_partially_update_epic]] — `POST /rest/agile/1.0/epic/{epicIdOrKey}` — Partially update epic ✏️
- [[jsw_get_issues_for_epic]] — `GET /rest/agile/1.0/epic/{epicIdOrKey}/issue` — Get issues for epic
- [[jsw_move_issues_to_epic]] — `POST /rest/agile/1.0/epic/{epicIdOrKey}/issue` — Move issues to epic ✏️
- [[jsw_get_issues_for_epic_enhanced]] — `GET /rest/software/1.0/epic/{epicIdOrKey}/issue` — Get issues for epic (enhanced)
- [[jsw_rank_epics]] — `PUT /rest/agile/1.0/epic/{epicIdOrKey}/rank` — Rank epics ✏️

## Issue

- [[jsw_rank_issues]] — `PUT /rest/agile/1.0/issue/rank` — Rank issues ✏️
- [[jsw_get_issue]] — `GET /rest/agile/1.0/issue/{issueIdOrKey}` — Get issue
- [[jsw_get_issue_estimation_for_board]] — `GET /rest/agile/1.0/issue/{issueIdOrKey}/estimation` — Get issue estimation for board
- [[jsw_estimate_issue_for_board]] — `PUT /rest/agile/1.0/issue/{issueIdOrKey}/estimation` — Estimate issue for board ✏️

## Sprint

- [[jsw_create_sprint]] — `POST /rest/agile/1.0/sprint` — Create sprint ✏️
- [[jsw_get_sprint]] — `GET /rest/agile/1.0/sprint/{sprintId}` — Get sprint
- [[jsw_update_sprint]] — `PUT /rest/agile/1.0/sprint/{sprintId}` — Update sprint ✏️
- [[jsw_partially_update_sprint]] — `POST /rest/agile/1.0/sprint/{sprintId}` — Partially update sprint ✏️
- [[jsw_delete_sprint]] — `DELETE /rest/agile/1.0/sprint/{sprintId}` — Delete sprint ✏️
- [[jsw_get_issues_for_sprint]] — `GET /rest/agile/1.0/sprint/{sprintId}/issue` — Get issues for sprint ⭐
- [[jsw_move_issues_to_sprint_and_rank]] — `POST /rest/agile/1.0/sprint/{sprintId}/issue` — Move issues to sprint and rank ✏️
- [[jsw_get_issues_for_sprint_enhanced]] — `GET /rest/software/1.0/sprint/{sprintId}/issue` — Get issues for sprint (enhanced)
- [[jsw_get_properties_keys]] — `GET /rest/agile/1.0/sprint/{sprintId}/properties` — Get properties keys
- [[jsw_get_property]] — `GET /rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey}` — Get property
- [[jsw_set_property]] — `PUT /rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey}` — Set property ✏️
- [[jsw_delete_property]] — `DELETE /rest/agile/1.0/sprint/{sprintId}/properties/{propertyKey}` — Delete property ✏️
- [[jsw_swap_sprint]] — `POST /rest/agile/1.0/sprint/{sprintId}/swap` — Swap sprint ✏️

## Development Information

- [[JSW - Store development information]] — `POST /rest/devinfo/0.10/bulk` — Store development information ✏️🔒
- [[JSW - Get repository]] — `GET /rest/devinfo/0.10/repository/{repositoryId}` — Get repository 🔒
- [[JSW - Delete repository]] — `DELETE /rest/devinfo/0.10/repository/{repositoryId}` — Delete repository ✏️🔒
- [[JSW - Delete development information by properties]] — `DELETE /rest/devinfo/0.10/bulkByProperties` — Delete development information by properties ✏️🔒
- [[JSW - Check if data exists for the supplied properties]] — `GET /rest/devinfo/0.10/existsByProperties` — Check if data exists for the supplied properties 🔒
- [[JSW - Delete development information entity]] — `DELETE /rest/devinfo/0.10/repository/{repositoryId}/{entityType}/{entityId}` — Delete development information entity ✏️🔒

## Feature Flags

- [[JSW - Submit Feature Flag data]] — `POST /rest/featureflags/0.1/bulk` — Submit Feature Flag data ✏️🔒
- [[JSW - Delete Feature Flags by Property]] — `DELETE /rest/featureflags/0.1/bulkByProperties` — Delete Feature Flags by Property ✏️🔒
- [[JSW - Get a Feature Flag by ID]] — `GET /rest/featureflags/0.1/flag/{featureFlagId}` — Get a Feature Flag by ID 🔒
- [[JSW - Delete a Feature Flag by ID]] — `DELETE /rest/featureflags/0.1/flag/{featureFlagId}` — Delete a Feature Flag by ID ✏️🔒

## Deployments

- [[JSW - Submit deployment data]] — `POST /rest/deployments/0.1/bulk` — Submit deployment data ✏️🔒
- [[JSW - Delete deployments by Property]] — `DELETE /rest/deployments/0.1/bulkByProperties` — Delete deployments by Property ✏️🔒
- [[JSW - Get a deployment by key]] — `GET /rest/deployments/0.1/pipelines/{pipelineId}/environments/{environmentId}/deployments/{deploymentSequenceNumber}` — Get a deployment by key 🔒
- [[JSW - Delete a deployment by key]] — `DELETE /rest/deployments/0.1/pipelines/{pipelineId}/environments/{environmentId}/deployments/{deploymentSequenceNumber}` — Delete a deployment by key ✏️🔒
- [[JSW - Get deployment gating status by key]] — `GET /rest/deployments/0.1/pipelines/{pipelineId}/environments/{environmentId}/deployments/{deploymentSequenceNumber}/gating-status` — Get deployment gating status by key 🔒

## Builds

- [[JSW - Submit build data]] — `POST /rest/builds/0.1/bulk` — Submit build data ✏️🔒
- [[JSW - Delete builds by Property]] — `DELETE /rest/builds/0.1/bulkByProperties` — Delete builds by Property ✏️🔒
- [[JSW - Get a build by key]] — `GET /rest/builds/0.1/pipelines/{pipelineId}/builds/{buildNumber}` — Get a build by key 🔒
- [[JSW - Delete a build by key]] — `DELETE /rest/builds/0.1/pipelines/{pipelineId}/builds/{buildNumber}` — Delete a build by key ✏️🔒

## Remote Links

- [[JSW - Submit Remote Link data]] — `POST /rest/remotelinks/1.0/bulk` — Submit Remote Link data ✏️🔒
- [[JSW - Delete Remote Links by Property]] — `DELETE /rest/remotelinks/1.0/bulkByProperties` — Delete Remote Links by Property ✏️🔒
- [[JSW - Get a Remote Link by ID]] — `GET /rest/remotelinks/1.0/remotelink/{remoteLinkId}` — Get a Remote Link by ID 🔒
- [[JSW - Delete a Remote Link by ID]] — `DELETE /rest/remotelinks/1.0/remotelink/{remoteLinkId}` — Delete a Remote Link by ID ✏️🔒

## Security Information

- [[JSW - Submit Security Workspaces to link]] — `POST /rest/security/1.0/linkedWorkspaces/bulk` — Submit Security Workspaces to link ✏️🔒
- [[JSW - Delete linked Security Workspaces]] — `DELETE /rest/security/1.0/linkedWorkspaces/bulk` — Delete linked Security Workspaces ✏️🔒
- [[JSW - Get linked Security Workspaces]] — `GET /rest/security/1.0/linkedWorkspaces` — Get linked Security Workspaces 🔒
- [[JSW - Get a linked Security Workspace by ID]] — `GET /rest/security/1.0/linkedWorkspaces/{workspaceId}` — Get a linked Security Workspace by ID 🔒
- [[JSW - Submit Vulnerability data]] — `POST /rest/security/1.0/bulk` — Submit Vulnerability data ✏️🔒
- [[JSW - Delete Vulnerabilities by Property]] — `DELETE /rest/security/1.0/bulkByProperties` — Delete Vulnerabilities by Property ✏️🔒
- [[JSW - Get a Vulnerability by ID]] — `GET /rest/security/1.0/vulnerability/{vulnerabilityId}` — Get a Vulnerability by ID 🔒
- [[JSW - Delete a Vulnerability by ID]] — `DELETE /rest/security/1.0/vulnerability/{vulnerabilityId}` — Delete a Vulnerability by ID ✏️🔒

## Operations

- [[JSW - Submit Operations Workspace Ids]] — `POST /rest/operations/1.0/linkedWorkspaces/bulk` — Submit Operations Workspace Ids ✏️🔒
- [[JSW - Delete Operations Workpaces by Id]] — `DELETE /rest/operations/1.0/linkedWorkspaces/bulk` — Delete Operations Workpaces by Id ✏️🔒
- [[JSW - Get all Operations Workspace IDs or a specific Operations Workspace by ID]] — `GET /rest/operations/1.0/linkedWorkspaces` — Get all Operations Workspace IDs or a specific Operations Workspace by ID 🔒
- [[JSW - Submit Incident or Review data]] — `POST /rest/operations/1.0/bulk` — Submit Incident or Review data ✏️🔒
- [[JSW - Delete Incidents or Review by Property]] — `DELETE /rest/operations/1.0/bulkByProperties` — Delete Incidents or Review by Property ✏️🔒
- [[JSW - Get a Incident by ID]] — `GET /rest/operations/1.0/incidents/{incidentId}` — Get a Incident by ID 🔒
- [[JSW - Delete a Incident by ID]] — `DELETE /rest/operations/1.0/incidents/{incidentId}` — Delete a Incident by ID ✏️🔒
- [[JSW - Get a Review by ID]] — `GET /rest/operations/1.0/post-incident-reviews/{reviewId}` — Get a Review by ID 🔒
- [[JSW - Delete a Review by ID]] — `DELETE /rest/operations/1.0/post-incident-reviews/{reviewId}` — Delete a Review by ID ✏️🔒

## DevOps Components

- [[JSW - Submit DevOps Components]] — `POST /rest/devopscomponents/1.0/bulk` — Submit DevOps Components ✏️🔒
- [[JSW - Delete DevOps Components by Property]] — `DELETE /rest/devopscomponents/1.0/bulkByProperties` — Delete DevOps Components by Property ✏️🔒
- [[JSW - Get a Component by ID]] — `GET /rest/devopscomponents/1.0/devopscomponents/{componentId}` — Get a Component by ID 🔒
- [[JSW - Delete a Component by ID]] — `DELETE /rest/devopscomponents/1.0/devopscomponents/{componentId}` — Delete a Component by ID ✏️🔒
