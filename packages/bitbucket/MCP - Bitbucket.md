---
tags:
  - moc
  - mcp
  - api/app/bitbucket
up: "[[MCP Tools]]"
---
# MCP - Bitbucket

- **Tools:** 265 (exposed: 7; the others via `run_vault_tool`)
- **Requests only:** 3
- **Instance:** `instance` parameter — notes tagged `bitbucket/workspace`
- **Official documentation:** https://developer.atlassian.com/cloud/bitbucket/rest/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Addon

- [[Bitbucket - Update an installed app]] — `PUT /addon` — Update an installed app ✏️🔒
- [[Bitbucket - Delete an app]] — `DELETE /addon` — Delete an app ✏️🔒
- [[Bitbucket - Get the client key of a Connect addon]] — `GET /addon/{addon_key}/client-key` — Get the client key of a Connect addon 🔒

## Branch restrictions

- [[bitbucket_list_branch_restrictions]] — `GET /repositories/{workspace}/{repo_slug}/branch-restrictions` — List branch restrictions
- [[bitbucket_create_a_branch_restriction_rule]] — `POST /repositories/{workspace}/{repo_slug}/branch-restrictions` — Create a branch restriction rule ✏️
- [[bitbucket_get_a_branch_restriction_rule]] — `GET /repositories/{workspace}/{repo_slug}/branch-restrictions/{id}` — Get a branch restriction rule
- [[bitbucket_update_a_branch_restriction_rule]] — `PUT /repositories/{workspace}/{repo_slug}/branch-restrictions/{id}` — Update a branch restriction rule ✏️
- [[bitbucket_delete_a_branch_restriction_rule]] — `DELETE /repositories/{workspace}/{repo_slug}/branch-restrictions/{id}` — Delete a branch restriction rule ✏️

## Branching model

- [[bitbucket_get_the_branching_model_for_a_repository]] — `GET /repositories/{workspace}/{repo_slug}/branching-model` — Get the branching model for a repository
- [[bitbucket_get_the_branching_model_config_for_a_repository]] — `GET /repositories/{workspace}/{repo_slug}/branching-model/settings` — Get the branching model config for a repository
- [[bitbucket_update_the_branching_model_config_for_a_repository]] — `PUT /repositories/{workspace}/{repo_slug}/branching-model/settings` — Update the branching model config for a repository ✏️
- [[bitbucket_get_the_effective_or_currently_applied_branching_model]] — `GET /repositories/{workspace}/{repo_slug}/effective-branching-model` — Get the effective, or currently applied, branching model for a repository
- [[bitbucket_get_the_branching_model_for_a_project]] — `GET /workspaces/{workspace}/projects/{project_key}/branching-model` — Get the branching model for a project
- [[bitbucket_get_the_branching_model_config_for_a_project]] — `GET /workspaces/{workspace}/projects/{project_key}/branching-model/settings` — Get the branching model config for a project
- [[bitbucket_update_the_branching_model_config_for_a_project]] — `PUT /workspaces/{workspace}/projects/{project_key}/branching-model/settings` — Update the branching model config for a project ✏️

## Commit statuses

- [[bitbucket_list_commit_statuses_for_a_commit]] — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses` — List commit statuses for a commit
- [[bitbucket_create_a_build_status_for_a_commit]] — `POST /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build` — Create a build status for a commit ✏️
- [[bitbucket_get_a_build_status_for_a_commit]] — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key}` — Get a build status for a commit
- [[bitbucket_update_a_build_status_for_a_commit]] — `PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key}` — Update a build status for a commit ✏️

## Commits

- [[bitbucket_get_a_commit]] — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}` — Get a commit
- [[bitbucket_approve_a_commit]] — `POST /repositories/{workspace}/{repo_slug}/commit/{commit}/approve` — Approve a commit ✏️
- [[bitbucket_unapprove_a_commit]] — `DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/approve` — Unapprove a commit ✏️
- [[bitbucket_list_a_commit_s_comments]] — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/comments` — List a commit's comments
- [[bitbucket_create_comment_for_a_commit]] — `POST /repositories/{workspace}/{repo_slug}/commit/{commit}/comments` — Create comment for a commit ✏️
- [[bitbucket_get_a_commit_comment]] — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}` — Get a commit comment
- [[bitbucket_update_a_commit_comment]] — `PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}` — Update a commit comment ✏️
- [[bitbucket_delete_a_commit_comment]] — `DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}` — Delete a commit comment ✏️
- [[bitbucket_list_commits]] — `GET /repositories/{workspace}/{repo_slug}/commits` — List commits ⭐
- [[bitbucket_list_commits_with_include_exclude]] — `POST /repositories/{workspace}/{repo_slug}/commits` — List commits with include/exclude
- [[bitbucket_list_commits_for_revision]] — `GET /repositories/{workspace}/{repo_slug}/commits/{revision}` — List commits for revision
- [[bitbucket_list_commits_for_revision_using_include_exclude]] — `POST /repositories/{workspace}/{repo_slug}/commits/{revision}` — List commits for revision using include/exclude
- [[bitbucket_compare_two_commits]] — `GET /repositories/{workspace}/{repo_slug}/diff/{spec}` — Compare two commits
- [[bitbucket_compare_two_commit_diff_stats]] — `GET /repositories/{workspace}/{repo_slug}/diffstat/{spec}` — Compare two commit diff stats
- [[bitbucket_get_file_conflicts_for_a_commit_spec]] — `GET /repositories/{workspace}/{repo_slug}/file-conflicts/{spec}` — Get file conflicts for a commit spec
- [[bitbucket_get_the_common_ancestor_between_two_commits]] — `GET /repositories/{workspace}/{repo_slug}/merge-base/{revspec}` — Get the common ancestor between two commits
- [[bitbucket_get_a_patch_for_two_commits]] — `GET /repositories/{workspace}/{repo_slug}/patch/{spec}` — Get a patch for two commits

## Deployments

- [[bitbucket_list_repository_deploy_keys]] — `GET /repositories/{workspace}/{repo_slug}/deploy-keys` — List repository deploy keys
- [[bitbucket_add_a_repository_deploy_key]] — `POST /repositories/{workspace}/{repo_slug}/deploy-keys` — Add a repository deploy key ✏️
- [[bitbucket_get_a_repository_deploy_key]] — `GET /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}` — Get a repository deploy key
- [[bitbucket_update_a_repository_deploy_key]] — `PUT /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}` — Update a repository deploy key ✏️
- [[bitbucket_delete_a_repository_deploy_key]] — `DELETE /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}` — Delete a repository deploy key ✏️
- [[bitbucket_list_deployments]] — `GET /repositories/{workspace}/{repo_slug}/deployments` — List deployments
- [[bitbucket_get_a_deployment]] — `GET /repositories/{workspace}/{repo_slug}/deployments/{deployment_uuid}` — Get a deployment
- [[bitbucket_list_environments]] — `GET /repositories/{workspace}/{repo_slug}/environments` — List environments
- [[bitbucket_create_an_environment]] — `POST /repositories/{workspace}/{repo_slug}/environments` — Create an environment ✏️
- [[bitbucket_get_an_environment]] — `GET /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}` — Get an environment
- [[bitbucket_delete_an_environment]] — `DELETE /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}` — Delete an environment ✏️
- [[bitbucket_update_an_environment]] — `POST /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes` — Update an environment ✏️
- [[bitbucket_list_project_deploy_keys]] — `GET /workspaces/{workspace}/projects/{project_key}/deploy-keys` — List project deploy keys
- [[bitbucket_create_a_project_deploy_key]] — `POST /workspaces/{workspace}/projects/{project_key}/deploy-keys` — Create a project deploy key ✏️
- [[bitbucket_get_a_project_deploy_key]] — `GET /workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id}` — Get a project deploy key
- [[bitbucket_delete_a_deploy_key_from_a_project]] — `DELETE /workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id}` — Delete a deploy key from a project ✏️

## Downloads

- [[bitbucket_list_download_artifacts]] — `GET /repositories/{workspace}/{repo_slug}/downloads` — List download artifacts
- [[bitbucket_upload_a_download_artifact]] — `POST /repositories/{workspace}/{repo_slug}/downloads` — Upload a download artifact ✏️
- [[bitbucket_get_a_download_artifact_link]] — `GET /repositories/{workspace}/{repo_slug}/downloads/{filename}` — Get a download artifact link
- [[bitbucket_delete_a_download_artifact]] — `DELETE /repositories/{workspace}/{repo_slug}/downloads/{filename}` — Delete a download artifact ✏️

## GPG

- [[bitbucket_list_gpg_keys]] — `GET /users/{selected_user}/gpg-keys` — List GPG keys
- [[bitbucket_add_a_new_gpg_key]] — `POST /users/{selected_user}/gpg-keys` — Add a new GPG key ✏️
- [[bitbucket_get_a_gpg_key]] — `GET /users/{selected_user}/gpg-keys/{fingerprint}` — Get a GPG key
- [[bitbucket_delete_a_gpg_key]] — `DELETE /users/{selected_user}/gpg-keys/{fingerprint}` — Delete a GPG key ✏️

## Pipelines

- [[bitbucket_list_variables_for_an_environment]] — `GET /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables` — List variables for an environment
- [[bitbucket_create_a_variable_for_an_environment]] — `POST /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables` — Create a variable for an environment ✏️
- [[bitbucket_update_a_variable_for_an_environment]] — `PUT /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid}` — Update a variable for an environment ✏️
- [[bitbucket_delete_a_variable_for_an_environment]] — `DELETE /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid}` — Delete a variable for an environment ✏️
- [[bitbucket_list_pipelines]] — `GET /repositories/{workspace}/{repo_slug}/pipelines` — List pipelines
- [[bitbucket_run_a_pipeline]] — `POST /repositories/{workspace}/{repo_slug}/pipelines` — Run a pipeline ✏️
- [[bitbucket_list_caches]] — `GET /repositories/{workspace}/{repo_slug}/pipelines-config/caches` — List caches
- [[bitbucket_delete_caches]] — `DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/caches` — Delete caches ✏️
- [[bitbucket_delete_a_cache]] — `DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid}` — Delete a cache ✏️
- [[bitbucket_get_cache_content_uri]] — `GET /repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid}/content-uri` — Get cache content URI
- [[bitbucket_get_repository_runners]] — `GET /repositories/{workspace}/{repo_slug}/pipelines-config/runners` — Get repository runners
- [[bitbucket_create_repository_runner]] — `POST /repositories/{workspace}/{repo_slug}/pipelines-config/runners` — Create repository runner ✏️
- [[bitbucket_get_repository_runner]] — `GET /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}` — Get repository runner
- [[bitbucket_update_repository_runner]] — `PUT /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}` — Update repository runner ✏️
- [[bitbucket_delete_repository_runner]] — `DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}` — Delete repository runner ✏️
- [[bitbucket_get_a_pipeline]] — `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}` — Get a pipeline
- [[bitbucket_list_steps_for_a_pipeline]] — `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps` — List steps for a pipeline
- [[bitbucket_get_a_step_of_a_pipeline]] — `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}` — Get a step of a pipeline
- [[bitbucket_get_log_file_for_a_step]] — `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/log` — Get log file for a step
- [[bitbucket_get_the_logs_for_the_build_container_or_a_service_cont]] — `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/logs/{log_uuid}` — Get the logs for the build container or a service container for a given step of a pipeline.
- [[bitbucket_get_a_summary_of_test_reports_for_a_given_step_of_a_pi]] — `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports` — Get a summary of test reports for a given step of a pipeline.
- [[bitbucket_get_test_cases_for_a_given_step_of_a_pipeline]] — `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases` — Get test cases for a given step of a pipeline.
- [[bitbucket_get_test_case_reasons_output_for_a_given_test_case_in]] — `GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases/{test_case_uuid}/test_case_reasons` — Get test case reasons (output) for a given test case in a step of a pipeline.
- [[bitbucket_stop_a_pipeline]] — `POST /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/stopPipeline` — Stop a pipeline ✏️
- [[bitbucket_get_configuration]] — `GET /repositories/{workspace}/{repo_slug}/pipelines_config` — Get configuration
- [[bitbucket_update_configuration]] — `PUT /repositories/{workspace}/{repo_slug}/pipelines_config` — Update configuration ✏️
- [[bitbucket_update_the_next_build_number]] — `PUT /repositories/{workspace}/{repo_slug}/pipelines_config/build_number` — Update the next build number ✏️
- [[bitbucket_list_schedules]] — `GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules` — List schedules
- [[bitbucket_create_a_schedule]] — `POST /repositories/{workspace}/{repo_slug}/pipelines_config/schedules` — Create a schedule ✏️
- [[bitbucket_get_a_schedule]] — `GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}` — Get a schedule
- [[bitbucket_update_a_schedule]] — `PUT /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}` — Update a schedule ✏️
- [[bitbucket_delete_a_schedule]] — `DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}` — Delete a schedule ✏️
- [[bitbucket_list_executions_of_a_schedule]] — `GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}/executions` — List executions of a schedule
- [[bitbucket_get_ssh_key_pair]] — `GET /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair` — Get SSH key pair
- [[bitbucket_update_ssh_key_pair]] — `PUT /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair` — Update SSH key pair ✏️
- [[bitbucket_delete_ssh_key_pair]] — `DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair` — Delete SSH key pair ✏️
- [[bitbucket_list_known_hosts]] — `GET /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts` — List known hosts
- [[bitbucket_create_a_known_host]] — `POST /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts` — Create a known host ✏️
- [[bitbucket_get_a_known_host]] — `GET /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}` — Get a known host
- [[bitbucket_update_a_known_host]] — `PUT /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}` — Update a known host ✏️
- [[bitbucket_delete_a_known_host]] — `DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}` — Delete a known host ✏️
- [[bitbucket_list_variables_for_a_repository]] — `GET /repositories/{workspace}/{repo_slug}/pipelines_config/variables` — List variables for a repository
- [[bitbucket_create_a_variable_for_a_repository]] — `POST /repositories/{workspace}/{repo_slug}/pipelines_config/variables` — Create a variable for a repository ✏️
- [[bitbucket_get_a_variable_for_a_repository]] — `GET /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid}` — Get a variable for a repository
- [[bitbucket_update_a_variable_for_a_repository]] — `PUT /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid}` — Update a variable for a repository ✏️
- [[bitbucket_delete_a_variable_for_a_repository]] — `DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid}` — Delete a variable for a repository ✏️
- [[bitbucket_get_openid_configuration_for_oidc_in_pipelines]] — `GET /workspaces/{workspace}/pipelines-config/identity/oidc/.well-known/openid-configuration` — Get OpenID configuration for OIDC in Pipelines
- [[bitbucket_get_keys_for_oidc_in_pipelines]] — `GET /workspaces/{workspace}/pipelines-config/identity/oidc/keys.json` — Get keys for OIDC in Pipelines
- [[bitbucket_get_workspace_runners]] — `GET /workspaces/{workspace}/pipelines-config/runners` — Get workspace runners
- [[bitbucket_create_workspace_runner]] — `POST /workspaces/{workspace}/pipelines-config/runners` — Create workspace runner ✏️
- [[bitbucket_get_workspace_runner]] — `GET /workspaces/{workspace}/pipelines-config/runners/{runner_uuid}` — Get workspace runner
- [[bitbucket_update_workspace_runner]] — `PUT /workspaces/{workspace}/pipelines-config/runners/{runner_uuid}` — Update workspace runner ✏️
- [[bitbucket_delete_workspace_runner]] — `DELETE /workspaces/{workspace}/pipelines-config/runners/{runner_uuid}` — Delete workspace runner ✏️
- [[bitbucket_list_variables_for_a_workspace]] — `GET /workspaces/{workspace}/pipelines-config/variables` — List variables for a workspace
- [[bitbucket_create_a_variable_for_a_workspace]] — `POST /workspaces/{workspace}/pipelines-config/variables` — Create a variable for a workspace ✏️
- [[bitbucket_get_variable_for_a_workspace]] — `GET /workspaces/{workspace}/pipelines-config/variables/{variable_uuid}` — Get variable for a workspace
- [[bitbucket_update_variable_for_a_workspace]] — `PUT /workspaces/{workspace}/pipelines-config/variables/{variable_uuid}` — Update variable for a workspace ✏️
- [[bitbucket_delete_a_variable_for_a_workspace]] — `DELETE /workspaces/{workspace}/pipelines-config/variables/{variable_uuid}` — Delete a variable for a workspace ✏️

## Projects

- [[bitbucket_create_a_project_in_a_workspace]] — `POST /workspaces/{workspace}/projects` — Create a project in a workspace ✏️
- [[bitbucket_get_a_project_for_a_workspace]] — `GET /workspaces/{workspace}/projects/{project_key}` — Get a project for a workspace
- [[bitbucket_update_a_project_for_a_workspace]] — `PUT /workspaces/{workspace}/projects/{project_key}` — Update a project for a workspace ✏️
- [[bitbucket_delete_a_project_for_a_workspace]] — `DELETE /workspaces/{workspace}/projects/{project_key}` — Delete a project for a workspace ✏️
- [[bitbucket_list_the_default_reviewers_in_a_project]] — `GET /workspaces/{workspace}/projects/{project_key}/default-reviewers` — List the default reviewers in a project
- [[bitbucket_get_a_default_reviewer]] — `GET /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}` — Get a default reviewer
- [[bitbucket_add_the_specific_user_as_a_default_reviewer_for_the_pr]] — `PUT /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}` — Add the specific user as a default reviewer for the project ✏️
- [[bitbucket_remove_the_specific_user_from_the_project_s_default_re]] — `DELETE /workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}` — Remove the specific user from the project's default reviewers ✏️
- [[bitbucket_list_explicit_group_permissions_for_a_project]] — `GET /workspaces/{workspace}/projects/{project_key}/permissions-config/groups` — List explicit group permissions for a project
- [[bitbucket_get_an_explicit_group_permission_for_a_project]] — `GET /workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}` — Get an explicit group permission for a project
- [[bitbucket_update_an_explicit_group_permission_for_a_project]] — `PUT /workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}` — Update an explicit group permission for a project ✏️
- [[bitbucket_delete_an_explicit_group_permission_for_a_project]] — `DELETE /workspaces/{workspace}/projects/{project_key}/permissions-config/groups/{group_slug}` — Delete an explicit group permission for a project ✏️
- [[bitbucket_list_explicit_user_permissions_for_a_project]] — `GET /workspaces/{workspace}/projects/{project_key}/permissions-config/users` — List explicit user permissions for a project
- [[bitbucket_get_an_explicit_user_permission_for_a_project]] — `GET /workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}` — Get an explicit user permission for a project
- [[bitbucket_update_an_explicit_user_permission_for_a_project]] — `PUT /workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}` — Update an explicit user permission for a project ✏️
- [[bitbucket_delete_an_explicit_user_permission_for_a_project]] — `DELETE /workspaces/{workspace}/projects/{project_key}/permissions-config/users/{selected_user_id}` — Delete an explicit user permission for a project ✏️

## Pullrequests

- [[bitbucket_list_pull_requests_that_contain_a_commit]] — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/pullrequests` — List pull requests that contain a commit
- [[bitbucket_list_default_reviewers]] — `GET /repositories/{workspace}/{repo_slug}/default-reviewers` — List default reviewers
- [[bitbucket_get_a_default_reviewer_get]] — `GET /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}` — Get a default reviewer
- [[bitbucket_add_a_user_to_the_default_reviewers]] — `PUT /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}` — Add a user to the default reviewers ✏️
- [[bitbucket_remove_a_user_from_the_default_reviewers]] — `DELETE /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}` — Remove a user from the default reviewers ✏️
- [[bitbucket_list_effective_default_reviewers]] — `GET /repositories/{workspace}/{repo_slug}/effective-default-reviewers` — List effective default reviewers
- [[bitbucket_list_pull_requests]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests` — List pull requests ⭐
- [[bitbucket_create_a_pull_request]] — `POST /repositories/{workspace}/{repo_slug}/pullrequests` — Create a pull request ✏️
- [[bitbucket_list_a_pull_request_activity_log]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests/activity` — List a pull request activity log
- [[bitbucket_get_a_pull_request]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}` — Get a pull request ⭐
- [[bitbucket_update_a_pull_request]] — `PUT /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}` — Update a pull request ✏️
- [[bitbucket_list_a_pull_request_activity_log_get]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/activity` — List a pull request activity log
- [[bitbucket_approve_a_pull_request]] — `POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve` — Approve a pull request ✏️
- [[bitbucket_unapprove_a_pull_request]] — `DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/approve` — Unapprove a pull request ✏️
- [[bitbucket_list_comments_on_a_pull_request]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments` — List comments on a pull request
- [[bitbucket_create_a_comment_on_a_pull_request]] — `POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments` — Create a comment on a pull request ✏️
- [[bitbucket_get_a_comment_on_a_pull_request]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}` — Get a comment on a pull request
- [[bitbucket_update_a_comment_on_a_pull_request]] — `PUT /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}` — Update a comment on a pull request ✏️
- [[bitbucket_delete_a_comment_on_a_pull_request]] — `DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}` — Delete a comment on a pull request ✏️
- [[bitbucket_resolve_a_comment_thread]] — `POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}/resolve` — Resolve a comment thread ✏️
- [[bitbucket_reopen_a_comment_thread]] — `DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}/resolve` — Reopen a comment thread ✏️
- [[bitbucket_list_commits_on_a_pull_request]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/commits` — List commits on a pull request
- [[bitbucket_get_file_conflicts_for_a_pull_request]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/conflicts` — Get file conflicts for a pull request
- [[bitbucket_decline_a_pull_request]] — `POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/decline` — Decline a pull request ✏️
- [[bitbucket_list_changes_in_a_pull_request]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff` — List changes in a pull request
- [[bitbucket_get_the_diff_stat_for_a_pull_request]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diffstat` — Get the diff stat for a pull request
- [[bitbucket_merge_a_pull_request]] — `POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge` — Merge a pull request ✏️
- [[bitbucket_get_the_merge_task_status_for_a_pull_request]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge/task-status/{task_id}` — Get the merge task status for a pull request
- [[bitbucket_get_the_patch_for_a_pull_request]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/patch` — Get the patch for a pull request
- [[bitbucket_request_changes_for_a_pull_request]] — `POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/request-changes` — Request changes for a pull request ✏️
- [[bitbucket_remove_change_request_for_a_pull_request]] — `DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/request-changes` — Remove change request for a pull request ✏️
- [[bitbucket_list_commit_statuses_for_a_pull_request]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/statuses` — List commit statuses for a pull request
- [[bitbucket_list_tasks_on_a_pull_request]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks` — List tasks on a pull request
- [[bitbucket_create_a_task_on_a_pull_request]] — `POST /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks` — Create a task on a pull request ✏️
- [[bitbucket_get_a_task_on_a_pull_request]] — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}` — Get a task on a pull request
- [[bitbucket_update_a_task_on_a_pull_request]] — `PUT /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}` — Update a task on a pull request ✏️
- [[bitbucket_delete_a_task_on_a_pull_request]] — `DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks/{task_id}` — Delete a task on a pull request ✏️

## Refs

- [[bitbucket_list_branches_and_tags]] — `GET /repositories/{workspace}/{repo_slug}/refs` — List branches and tags ⭐
- [[bitbucket_list_open_branches]] — `GET /repositories/{workspace}/{repo_slug}/refs/branches` — List open branches
- [[bitbucket_create_a_branch]] — `POST /repositories/{workspace}/{repo_slug}/refs/branches` — Create a branch ✏️
- [[bitbucket_get_a_branch]] — `GET /repositories/{workspace}/{repo_slug}/refs/branches/{name}` — Get a branch
- [[bitbucket_delete_a_branch]] — `DELETE /repositories/{workspace}/{repo_slug}/refs/branches/{name}` — Delete a branch ✏️
- [[bitbucket_list_tags]] — `GET /repositories/{workspace}/{repo_slug}/refs/tags` — List tags
- [[bitbucket_create_a_tag]] — `POST /repositories/{workspace}/{repo_slug}/refs/tags` — Create a tag ✏️
- [[bitbucket_get_a_tag]] — `GET /repositories/{workspace}/{repo_slug}/refs/tags/{name}` — Get a tag
- [[bitbucket_delete_a_tag]] — `DELETE /repositories/{workspace}/{repo_slug}/refs/tags/{name}` — Delete a tag ✏️

## Reports

- [[bitbucket_list_reports]] — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports` — List reports
- [[bitbucket_get_a_report]] — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}` — Get a report
- [[bitbucket_create_or_update_a_report]] — `PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}` — Create or update a report ✏️
- [[bitbucket_delete_a_report]] — `DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}` — Delete a report ✏️
- [[bitbucket_list_annotations]] — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations` — List annotations
- [[bitbucket_bulk_create_or_update_annotations]] — `POST /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations` — Bulk create or update annotations ✏️
- [[bitbucket_get_an_annotation]] — `GET /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}` — Get an annotation
- [[bitbucket_create_or_update_an_annotation]] — `PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}` — Create or update an annotation ✏️
- [[bitbucket_delete_an_annotation]] — `DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}` — Delete an annotation ✏️

## Repositories

- [[bitbucket_list_repositories_in_a_workspace]] — `GET /repositories/{workspace}` — List repositories in a workspace ⭐
- [[bitbucket_get_a_repository]] — `GET /repositories/{workspace}/{repo_slug}` — Get a repository ⭐
- [[bitbucket_update_a_repository]] — `PUT /repositories/{workspace}/{repo_slug}` — Update a repository ✏️
- [[bitbucket_create_a_repository]] — `POST /repositories/{workspace}/{repo_slug}` — Create a repository ✏️
- [[bitbucket_delete_a_repository]] — `DELETE /repositories/{workspace}/{repo_slug}` — Delete a repository ✏️
- [[bitbucket_list_repository_forks]] — `GET /repositories/{workspace}/{repo_slug}/forks` — List repository forks
- [[bitbucket_fork_a_repository]] — `POST /repositories/{workspace}/{repo_slug}/forks` — Fork a repository ✏️
- [[bitbucket_list_webhooks_for_a_repository]] — `GET /repositories/{workspace}/{repo_slug}/hooks` — List webhooks for a repository
- [[bitbucket_create_a_webhook_for_a_repository]] — `POST /repositories/{workspace}/{repo_slug}/hooks` — Create a webhook for a repository ✏️
- [[bitbucket_get_a_webhook_for_a_repository]] — `GET /repositories/{workspace}/{repo_slug}/hooks/{uid}` — Get a webhook for a repository
- [[bitbucket_update_a_webhook_for_a_repository]] — `PUT /repositories/{workspace}/{repo_slug}/hooks/{uid}` — Update a webhook for a repository ✏️
- [[bitbucket_delete_a_webhook_for_a_repository]] — `DELETE /repositories/{workspace}/{repo_slug}/hooks/{uid}` — Delete a webhook for a repository ✏️
- [[bitbucket_retrieve_the_inheritance_state_for_repository_settings]] — `GET /repositories/{workspace}/{repo_slug}/override-settings` — Retrieve the inheritance state for repository settings
- [[bitbucket_set_the_inheritance_state_for_repository_settings]] — `PUT /repositories/{workspace}/{repo_slug}/override-settings` — Set the inheritance state for repository settings ✏️
- [[bitbucket_list_explicit_group_permissions_for_a_repository]] — `GET /repositories/{workspace}/{repo_slug}/permissions-config/groups` — List explicit group permissions for a repository
- [[bitbucket_get_an_explicit_group_permission_for_a_repository]] — `GET /repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}` — Get an explicit group permission for a repository
- [[bitbucket_update_an_explicit_group_permission_for_a_repository]] — `PUT /repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}` — Update an explicit group permission for a repository ✏️
- [[bitbucket_delete_an_explicit_group_permission_for_a_repository]] — `DELETE /repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}` — Delete an explicit group permission for a repository ✏️
- [[bitbucket_list_explicit_user_permissions_for_a_repository]] — `GET /repositories/{workspace}/{repo_slug}/permissions-config/users` — List explicit user permissions for a repository
- [[bitbucket_get_an_explicit_user_permission_for_a_repository]] — `GET /repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}` — Get an explicit user permission for a repository
- [[bitbucket_update_an_explicit_user_permission_for_a_repository]] — `PUT /repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}` — Update an explicit user permission for a repository ✏️
- [[bitbucket_delete_an_explicit_user_permission_for_a_repository]] — `DELETE /repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}` — Delete an explicit user permission for a repository ✏️
- [[bitbucket_list_repositories_watchers]] — `GET /repositories/{workspace}/{repo_slug}/watchers` — List repositories watchers
- [[bitbucket_list_repository_permissions_in_a_workspace_for_a_user]] — `GET /user/workspaces/{workspace}/permissions/repositories` — List repository permissions in a workspace for a user

## SSH

- [[bitbucket_list_ssh_keys]] — `GET /users/{selected_user}/ssh-keys` — List SSH keys
- [[bitbucket_add_a_new_ssh_key]] — `POST /users/{selected_user}/ssh-keys` — Add a new SSH key ✏️
- [[bitbucket_get_a_ssh_key]] — `GET /users/{selected_user}/ssh-keys/{key_id}` — Get a SSH key
- [[bitbucket_update_a_ssh_key]] — `PUT /users/{selected_user}/ssh-keys/{key_id}` — Update a SSH key ✏️
- [[bitbucket_delete_a_ssh_key]] — `DELETE /users/{selected_user}/ssh-keys/{key_id}` — Delete a SSH key ✏️

## Snippets

- [[bitbucket_create_a_snippet]] — `POST /snippets` — Create a snippet ✏️
- [[bitbucket_list_snippets_in_a_workspace]] — `GET /snippets/{workspace}` — List snippets in a workspace
- [[bitbucket_create_a_snippet_for_a_workspace]] — `POST /snippets/{workspace}` — Create a snippet for a workspace ✏️
- [[bitbucket_get_a_snippet]] — `GET /snippets/{workspace}/{encoded_id}` — Get a snippet
- [[bitbucket_update_a_snippet]] — `PUT /snippets/{workspace}/{encoded_id}` — Update a snippet ✏️
- [[bitbucket_delete_a_snippet]] — `DELETE /snippets/{workspace}/{encoded_id}` — Delete a snippet ✏️
- [[bitbucket_list_comments_on_a_snippet]] — `GET /snippets/{workspace}/{encoded_id}/comments` — List comments on a snippet
- [[bitbucket_create_a_comment_on_a_snippet]] — `POST /snippets/{workspace}/{encoded_id}/comments` — Create a comment on a snippet ✏️
- [[bitbucket_get_a_comment_on_a_snippet]] — `GET /snippets/{workspace}/{encoded_id}/comments/{comment_id}` — Get a comment on a snippet
- [[bitbucket_update_a_comment_on_a_snippet]] — `PUT /snippets/{workspace}/{encoded_id}/comments/{comment_id}` — Update a comment on a snippet ✏️
- [[bitbucket_delete_a_comment_on_a_snippet]] — `DELETE /snippets/{workspace}/{encoded_id}/comments/{comment_id}` — Delete a comment on a snippet ✏️
- [[bitbucket_list_snippet_changes]] — `GET /snippets/{workspace}/{encoded_id}/commits` — List snippet changes
- [[bitbucket_get_a_previous_snippet_change]] — `GET /snippets/{workspace}/{encoded_id}/commits/{revision}` — Get a previous snippet change
- [[bitbucket_get_a_snippet_s_raw_file_at_head]] — `GET /snippets/{workspace}/{encoded_id}/files/{path}` — Get a snippet's raw file at HEAD
- [[bitbucket_check_if_the_current_user_is_watching_a_snippet]] — `GET /snippets/{workspace}/{encoded_id}/watch` — Check if the current user is watching a snippet
- [[bitbucket_watch_a_snippet]] — `PUT /snippets/{workspace}/{encoded_id}/watch` — Watch a snippet ✏️
- [[bitbucket_stop_watching_a_snippet]] — `DELETE /snippets/{workspace}/{encoded_id}/watch` — Stop watching a snippet ✏️
- [[bitbucket_list_users_watching_a_snippet]] — `GET /snippets/{workspace}/{encoded_id}/watchers` — List users watching a snippet
- [[bitbucket_get_a_previous_revision_of_a_snippet]] — `GET /snippets/{workspace}/{encoded_id}/{node_id}` — Get a previous revision of a snippet
- [[bitbucket_update_a_previous_revision_of_a_snippet]] — `PUT /snippets/{workspace}/{encoded_id}/{node_id}` — Update a previous revision of a snippet ✏️
- [[bitbucket_delete_a_previous_revision_of_a_snippet]] — `DELETE /snippets/{workspace}/{encoded_id}/{node_id}` — Delete a previous revision of a snippet ✏️
- [[bitbucket_get_a_snippet_s_raw_file]] — `GET /snippets/{workspace}/{encoded_id}/{node_id}/files/{path}` — Get a snippet's raw file
- [[bitbucket_get_snippet_changes_between_versions]] — `GET /snippets/{workspace}/{encoded_id}/{revision}/diff` — Get snippet changes between versions
- [[bitbucket_get_snippet_patch_between_versions]] — `GET /snippets/{workspace}/{encoded_id}/{revision}/patch` — Get snippet patch between versions

## Source

- [[bitbucket_list_commits_that_modified_a_file]] — `GET /repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path}` — List commits that modified a file
- [[bitbucket_get_the_root_directory_of_the_main_branch]] — `GET /repositories/{workspace}/{repo_slug}/src` — Get the root directory of the main branch
- [[bitbucket_create_a_commit_by_uploading_a_file]] — `POST /repositories/{workspace}/{repo_slug}/src` — Create a commit by uploading a file ✏️
- [[bitbucket_get_file_or_directory_contents]] — `GET /repositories/{workspace}/{repo_slug}/src/{commit}/{path}` — Get file or directory contents

## Users

- [[bitbucket_get_current_user]] — `GET /user` — Get current user ⭐
- [[bitbucket_list_email_addresses_for_current_user]] — `GET /user/emails` — List email addresses for current user
- [[bitbucket_get_an_email_address_for_current_user]] — `GET /user/emails/{email}` — Get an email address for current user
- [[bitbucket_get_a_user]] — `GET /users/{selected_user}` — Get a user

## Webhooks

- [[bitbucket_get_a_webhook_resource]] — `GET /hook_events` — Get a webhook resource
- [[bitbucket_list_subscribable_webhook_types]] — `GET /hook_events/{subject_type}` — List subscribable webhook types

## Workspaces

- [[bitbucket_list_workspaces_for_the_current_user]] — `GET /user/workspaces` — List workspaces for the current user
- [[bitbucket_get_user_permission_on_a_workspace]] — `GET /user/workspaces/{workspace}/permission` — Get user permission on a workspace
- [[bitbucket_get_a_workspace]] — `GET /workspaces/{workspace}` — Get a workspace
- [[bitbucket_list_webhooks_for_a_workspace]] — `GET /workspaces/{workspace}/hooks` — List webhooks for a workspace
- [[bitbucket_create_a_webhook_for_a_workspace]] — `POST /workspaces/{workspace}/hooks` — Create a webhook for a workspace ✏️
- [[bitbucket_get_a_webhook_for_a_workspace]] — `GET /workspaces/{workspace}/hooks/{uid}` — Get a webhook for a workspace
- [[bitbucket_update_a_webhook_for_a_workspace]] — `PUT /workspaces/{workspace}/hooks/{uid}` — Update a webhook for a workspace ✏️
- [[bitbucket_delete_a_webhook_for_a_workspace]] — `DELETE /workspaces/{workspace}/hooks/{uid}` — Delete a webhook for a workspace ✏️
- [[bitbucket_list_users_in_a_workspace]] — `GET /workspaces/{workspace}/members` — List users in a workspace
- [[bitbucket_get_user_membership_for_a_workspace]] — `GET /workspaces/{workspace}/members/{member}` — Get user membership for a workspace
- [[bitbucket_list_user_permissions_in_a_workspace]] — `GET /workspaces/{workspace}/permissions` — List user permissions in a workspace
- [[bitbucket_list_all_repository_permissions_for_a_workspace]] — `GET /workspaces/{workspace}/permissions/repositories` — List all repository permissions for a workspace
- [[bitbucket_list_a_repository_permissions_for_a_workspace]] — `GET /workspaces/{workspace}/permissions/repositories/{repo_slug}` — List a repository permissions for a workspace
- [[bitbucket_list_projects_in_a_workspace]] — `GET /workspaces/{workspace}/projects` — List projects in a workspace
- [[bitbucket_list_workspace_pull_requests_for_a_user]] — `GET /workspaces/{workspace}/pullrequests/{selected_user}` — List workspace pull requests for a user
- [[bitbucket_get_the_workspace_system_gpg_public_key_s]] — `GET /workspaces/{workspace}/settings/gpg/public-key` — Get the workspace system GPG public key(s)
