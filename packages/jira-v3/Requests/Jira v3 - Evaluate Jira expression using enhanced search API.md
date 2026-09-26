---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/jira-expressions
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/expression/evaluate"
category: "Jira expressions"
writes_data: false
tool_note: "[[jira_evaluate_jira_expression_using_enhanced_search_api]]"
---
# Jira v3 - Evaluate Jira expression using enhanced search API

**Evaluate Jira expression using enhanced search API** — `POST /rest/api/3/expression/evaluate`

- Run by the tool [[jira_evaluate_jira_expression_using_enhanced_search_api]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/expression/evaluate?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts meta.complexity that returns information about the expression complexity.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "context": {
    "board": 10100,
    "custom": {
      "config": {
        "type": "json",
        "value": {
          "userId": "10002"
        }
      },
      "issuesList": [
        {
          "key": "ACJIRA-1471",
          "type": "issue"
        },
        {
          "id": 100001,
          "type": "issue"
        }
      ],
      "myUser": {
        "accountId": "100001",
        "type": "user"
      },
      "nullField": {
        "type": "json"
      }
    },
    "customerRequest": 1450,
    "issue": {
      "key": "ACJIRA-1470"
    },
    "issues": {
      "jql": {
        "maxResults": 100,
        "nextPageToken": "EgQIlMIC",
        "query": "project = HSP"
      }
    },
    "project": {
      "key": "ACJIRA"
    },
    "serviceDesk": 10023,
    "sprint": 10001
  },
  "expression": "{ key: issue.key, type: issue.issueType.name, links: issue.links.map(link => link.linkedIssue.id), listCustomVariable: issuesList.includes(issue), customVariables: myUser.accountId == config.userId}"
}
```

## Original description

Evaluates a Jira expression and returns its value. The difference between this and `eval` is that this endpoint uses the enhanced search API when evaluating JQL queries. This API is eventually consistent, unlike the strongly consistent `eval` API. This allows for better performance and scalability. In addition, this API's response for JQL evaluation is based on a scrolling view (backed by a `nextPageToken`) instead of a paginated view (backed by `startAt` and `totalCount`).

This resource can be used to test Jira expressions that you plan to use elsewhere, or to fetch data in a flexible way. Consult the [Jira expressions documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/) for more details.

#### Context variables ####

The following context variables are available to Jira expressions evaluated by this resource. Their presence depends on various factors; usually you need to manually request them in the context object sent in the payload, but some of them are added automatically under certain conditions.

 *  `user` ([User](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user)): The current user. Always available and equal to `null` if the request is anonymous.
 *  `app` ([App](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#app)): The [Connect app](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) that made the request. Available only for authenticated requests made by Connect apps (read more here: [Authentication for Connect apps](https://developer.atlassian.com/cloud/jira/platform/security-for-connect-apps/)).
 *  `issue` ([Issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue)): The current issue. Available only when the issue is provided in the request context object.
 *  `issues` ([List](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#list) of [Issues](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue)): A collection of issues matching a JQL query. Available only when JQL is provided in the request context object.
 *  `project` ([Project](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#project)): The current project. Available only when the project is provided in the request context object.
 *  `sprint` ([Sprint](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#sprint)): The current sprint. Available only when the sprint is provided in the request context object.
 *  `board` ([Board](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#board)): The current board. Available only when the board is provided in the request context object.
 *  `serviceDesk` ([ServiceDesk](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#servicedesk)): The current service desk. Available only when the service desk is provided in the request context object.
 *  `customerRequest` ([CustomerRequest](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#customerrequest)): The current customer request. Available only when the customer request is provided in the request context object.

In addition, you can pass custom context variables along with their types. You can then access them from the Jira expression by key. You can use the following variables in a custom context:

 *  `user`: A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user) specified as an Atlassian account ID.
 *  `issue`: An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue) specified by ID or key. All the fields of the issue object are available in the Jira expression.
 *  `json`: A JSON object containing custom content.
 *  `list`: A JSON list of `user`, `issue`, or `json` variable types.

This operation can be accessed anonymously.

**[Permissions](#permissions) required**: None. However, an expression may return different results for different users depending on their permissions. For example, different users may see different comments on the same issue.  
Permission to access Jira Software is required to access Jira Software context variables (`board` and `sprint`) or fields (for example, `issue.sprint`).
