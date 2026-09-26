---
tags:
  - api/request
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
app: "Bitbucket"
method: GET
path: "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/activity"
category: "Pullrequests"
writes_data: false
tool_note: "[[bitbucket_list_a_pull_request_activity_log_get]]"
---
# Bitbucket - List a pull request activity log (GET)

**List a pull request activity log** — `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/activity`

- Run by the tool [[bitbucket_list_a_pull_request_activity_log_get]].
- Official documentation: https://developer.atlassian.com/cloud/bitbucket/rest/

```http
GET {{service.url}}/repositories/{{service.workspace}}/{{param:repo_slug}}/pullrequests/{{param:pull_request_id}}/activity
Authorization: {{service.auth_token}}
```

## Parameters

- `repo_slug` (path, string, required) — Value of reposlug in the path.
- `pull_request_id` (path, string, required) — Value of pullrequestid in the path.

## Original description

Returns a paginated list of the pull request's activity log.

This handler serves both a v20 and internal endpoint. The v20 endpoint
returns reviewer comments, updates, approvals and request changes. The internal
endpoint includes those plus tasks and attachments.

Comments created on a file or a line of code have an inline property.

Comment example:
```
{
    "pagelen": 20,
    "values": [
        {
            "comment": {
                "links": {
                    "self": {
                        "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695/comments/118571088"
                    },
                    "html": {
                        "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695/_/diff#comment-118571088"
                    }
                },
                "deleted": false,
                "pullrequest": {
                    "type": "pullrequest",
                    "id": 5695,
                    "links": {
                        "self": {
                            "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"
                        },
                        "html": {
                            "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"
                        }
                    },
                    "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"
                },
                "content": {
                    "raw": "inline with to a dn from lines",
                    "markup": "markdown",
                    "html": "inline with to a dn from lines",
                    "type": "rendered"
                },
                "created_on": "2019-09-27T00:33:46.039178+00:00",
                "user": {
                    "display_name": "Name Lastname",
                    "uuid": "{}",
                    "links": {
                        "self": {
                            "href": "https://api.bitbucket.org/2.0/users/%7B%7D"
                        },
                        "html": {
                            "href": "https://bitbucket.org/%7B%7D/"
                        },
                        "avatar": {
                            "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128"
                        }
                    },
                    "type": "user",
                    "nickname": "Name",
                    "account_id": ""
                },
                "created_on": "2019-09-27T00:33:46.039178+00:00",
                "user": {
                    "display_name": "Name Lastname",
                    "uuid": "{}",
                    "links": {
                        "self": {
                            "href": "https://api.bitbucket.org/2.0/users/%7B%7D"
                        },
                        "html": {
                            "href": "https://bitbucket.org/%7B%7D/"
                        },
                        "avatar": {
                            "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128"
                        }
                    },
                    "type": "user",
                    "nickname": "Name",
                    "account_id": ""
                },
                "updated_on": "2019-09-27T00:33:46.055384+00:00",
                "inline": {
                    "context_lines": "",
                    "to": null,
                    "path": "",
                    "outdated": false,
                    "from": 211
                },
                "type": "pullrequest_comment",
                "id": 118571088
            },
            "pull_request": {
                "type": "pullrequest",
                "id": 5695,
                "links": {
                    "self": {
                        "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"
                    },
                    "html": {
                        "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"
                    }
                },
                "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"
            }
        }
    ]
}
```

Updates include a state property of OPEN, MERGED, or DECLINED.

Update example:
```
{
    "pagelen": 20,
    "values": [
        {
            "update": {
                "description": "",
                "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it",
                "destination": {
                    "commit": {
                        "type": "commit",
                        "hash": "6a2c16e4a152",
                        "links": {
                            "self": {
                                "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/6a2c16e4a152"
                            },
                            "html": {
                                "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/commits/6a2c16e4a152"
                            }
                        }
                    },
                    "branch": {
                        "name": "master"
                    },
                    "repository": {
                        "name": "Atlaskit-MK-2",
                        "type": "repository",
                        "full_name": "atlassian/atlaskit-mk-2",
                        "links": {
                            "self": {
                                "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2"
                            },
                            "html": {
                                "href": "https://bitbucket.org/atlassian/atlaskit-mk-2"
                            },
                            "avatar": {
                                "href": "https://bytebucket.org/ravatar/%7B%7D?ts=js"
                            }
                        },
                        "uuid": "{}"
                    }
                },
                "reason": "",
                "source": {
                    "commit": {
                        "type": "commit",
                        "hash": "728c8bad1813",
                        "links": {
                            "self": {
                                "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/728c8bad1813"
                            },
                            "html": {
                                "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/commits/728c8bad1813"
                            }
                        }
                    },
                    "branch": {
                        "name": "username/NONE-add-onClick-prop-for-accessibility"
                    },
                    "repository": {
                        "name": "Atlaskit-MK-2",
                        "type": "repository",
                        "full_name": "atlassian/atlaskit-mk-2",
                        "links": {
                            "self": {
                                "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2"
                            },
                            "html": {
                                "href": "https://bitbucket.org/atlassian/atlaskit-mk-2"
                            },
                            "avatar": {
                                "href": "https://bytebucket.org/ravatar/%7B%7D?ts=js"
                            }
                        },
                        "uuid": "{}"
                    }
                },
                "state": "OPEN",
                "author": {
                    "display_name": "Name Lastname",
                    "uuid": "{}",
                    "links": {
                        "self": {
                            "href": "https://api.bitbucket.org/2.0/users/%7B%7D"
                        },
                        "html": {
                            "href": "https://bitbucket.org/%7B%7D/"
                        },
                        "avatar": {
                            "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128"
                        }
                    },
                    "type": "user",
                    "nickname": "Name",
                    "account_id": ""
                },
                "date": "2019-05-10T06:48:25.305565+00:00"
            },
            "pull_request": {
                "type": "pullrequest",
                "id": 5695,
                "links": {
                    "self": {
                        "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"
                    },
                    "html": {
                        "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"
                    }
                },
                "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"
            }
        }
    ]
}
```

Approval example:
```
{
    "pagelen": 20,
    "values": [
        {
            "approval": {
                "date": "2019-09-27T00:37:19.849534+00:00",
                "pullrequest": {
                    "type": "pullrequest",
                    "id": 5695,
                    "links": {
                        "self": {
                            "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"
                        },
                        "html": {
                            "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"
                        }
                    },
                    "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"
                },
                "user": {
                    "display_name": "Name Lastname",
                    "uuid": "{}",
                    "links": {
                        "self": {
                            "href": "https://api.bitbucket.org/2.0/users/%7B%7D"
                        },
                        "html": {
                            "href": "https://bitbucket.org/%7B%7D/"
                        },
                        "avatar": {
                            "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128"
                        }
                    },
                    "type": "user",
                    "nickname": "Name",
                    "account_id": ""
                }
            },
            "pull_request": {
                "type": "pullrequest",
                "id": 5695,
                "links": {
                    "self": {
                        "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"
                    },
                    "html": {
                        "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"
                    }
                },
                "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"
            }
        }
    ]
}
```
