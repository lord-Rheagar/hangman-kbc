{
  "nodes": [
    {
      "parameters": {},
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [
        -340,
        160
      ],
      "id": "5510f0db-f2d5-445f-b282-b2a705367e1e",
      "name": "When clicking ‘Execute workflow’"
    },
    {
      "parameters": {
        "documentId": {
          "__rl": true,
          "value": "1l1Xznrmh2hENrmJR9AL_EmausYcH8N48OJH3ilTnkjM",
          "mode": "list",
          "cachedResultName": "Competitor Intelligence Dashboard",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1l1Xznrmh2hENrmJR9AL_EmausYcH8N48OJH3ilTnkjM/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": "gid=0",
          "mode": "list",
          "cachedResultName": "Sheet1",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1l1Xznrmh2hENrmJR9AL_EmausYcH8N48OJH3ilTnkjM/edit#gid=0"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.6,
      "position": [
        -60,
        -20
      ],
      "id": "84adb3d1-d4af-44b8-ab5b-117396ed6a87",
      "name": "Get row(s) in sheet",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "3WUfENHi9FEtJRGR",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.perplexity.ai/chat/completions",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "accept",
              "value": "application/json"
            }
          ]
        },
        "sendBody": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "model",
              "value": "sonar"
            },
            {
              "name": "messages[0].role",
              "value": "user"
            },
            {
              "name": "messages[0].content",
              "value": "=<prompt> You are tasked with analyzing a competitor using publicly available data. Your objective is to create a detailed competitive intelligence report that focuses on key business metrics. <target> Analyze the following competitor: {{ $json['Website URL'] }} </target> <focus_area> Research and document these key aspects: *Brand Positioning and market messaging *Product Updates and recent launches *User base and notable wins *Funding news, Investment rounds and financial status *Organizational growth anf hiring trends </focus_area> <research_guidelines> For each focus area: *Utilize only public information from credible sources *Prioritize data from past 8 months *Include specific metrics and timestamp *Note any information gaps clearly </research_guidelines> <data_sources> Acceptable sources include: *Official company websites *Press Releases *News articles *Industry reports *Social Media profiles *Social Media posts *Job Boards *Financial filings </data_source><formatting_requirements>Structure your report with: *Clear section headers *Bullet points for key findings *Timestamps for all updates *Data visualization where relevant </formatting_requirements> <compliance_notes> *Only use publicly accessible information *Avoid speculation or unverified claims *Document all information sources *Maintain research standars </compliance_notes> </prompt>"
            }
          ]
        },
        "options": {
          "redirect": {
            "redirect": {}
          }
        }
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [
        180,
        -160
      ],
      "id": "fd8cac64-c59c-4eac-b73c-a6b8e788dcc2",
      "name": "HTTP Request",
      "credentials": {
        "httpHeaderAuth": {
          "id": "tf3oWxJ0pTgqUgrt",
          "name": "Perplexity Header Bearer"
        }
      }
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.tavily.com/search",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendBody": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "query",
              "value": "=Find news from the last 7 days about:  {{ $json['Competitor Name'] }}, {{ $json['Website URL'] }}"
            },
            {
              "name": "search_depth",
              "value": "advanced"
            },
            {
              "name": "topic",
              "value": "news"
            },
            {
              "name": "max_results",
              "value": "10"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [
        180,
        40
      ],
      "id": "df9c8839-4ba0-4c8c-b370-518d4c61f668",
      "name": "HTTP Request1",
      "credentials": {
        "httpHeaderAuth": {
          "id": "3jDQYnUsP54ku4AU",
          "name": "Header Auth account"
        }
      }
    },
    {
      "parameters": {
        "mode": "combine",
        "combineBy": "combineByPosition",
        "options": {}
      },
      "type": "n8n-nodes-base.merge",
      "typeVersion": 3.2,
      "position": [
        480,
        -80
      ],
      "id": "73608244-7911-4c5f-8ee9-ab821acfef17",
      "name": "Merge"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "99f11658-4744-4b34-9a26-5092c6e81861",
              "name": "choices[0].message.content",
              "value": "={{ $json.choices[0].message.content }}",
              "type": "string"
            },
            {
              "id": "ee093cac-fbbe-4e7d-9610-30a78030d81d",
              "name": "search_results",
              "value": "={{ $json.results }}",
              "type": "array"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        740,
        -40
      ],
      "id": "55ad0d34-67a7-44d6-a76c-0530db6c9167",
      "name": "Edit Fields"
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=<input> \n1. Research data about the target: {{ $json.choices[0].message.content }}\n\n2. Recent news articles: {{ $json.search_results }}",
        "messages": {
          "messageValues": [
            {
              "message": "=You are tasked with analyzing two inputs and formatting them into a standardized intelligence report. \n\n<inputs> \n1. Research data from the target\n2. Recent news articles \n</inputs> \n\n<output>\nFormat your analysis using these exact headers\n\n##Market Position \n-Current status\n-Competitive Advantage \n-Target audience \n-Current no of users\n\n# Product \n-Current product offerings \n-Recent product launches \n-Pipeline developments \n- Latest user reviews \n\n# Positioning \n-Current market positioning\n-Market share captured \n-Promotional activities \n-Latest sponsorship and brand deals \n\n# Corporate Updates \n-Leadership changes \n-Strategic initiatives \n-Company announcements \n\n# Financial status \n-Funding rounds\n-Funding announcements\n-Revenue indicators \n-Market performance \n\n# Growth Metrics \n-Team size \n-Market expansion\n-Customer acquisition and marketing \n\n</output>\n\n<rules>\n-Inlcude dates for all developments \n-Note information gaps \n-Use bullet point for findings \n-Bold significant metrics \n</rules>\n"
            }
          ]
        },
        "batching": {}
      },
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "typeVersion": 1.7,
      "position": [
        960,
        -40
      ],
      "id": "4a1a2566-bf03-4f92-aab5-79652801a369",
      "name": "Basic LLM Chain"
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "value": "chatgpt-4o-latest",
          "mode": "list",
          "cachedResultName": "chatgpt-4o-latest"
        },
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1.2,
      "position": [
        1040,
        180
      ],
      "id": "b06777a0-3295-41bb-b593-bb71359c937f",
      "name": "OpenAI Chat Model",
      "credentials": {
        "openAiApi": {
          "id": "WyQd75lhtrt88ua3",
          "name": "OpenAi account 3"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1l1Xznrmh2hENrmJR9AL_EmausYcH8N48OJH3ilTnkjM",
          "mode": "list",
          "cachedResultName": "Competitor Intelligence Dashboard",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1l1Xznrmh2hENrmJR9AL_EmausYcH8N48OJH3ilTnkjM/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": "gid=0",
          "mode": "list",
          "cachedResultName": "Sheet1",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1l1Xznrmh2hENrmJR9AL_EmausYcH8N48OJH3ilTnkjM/edit#gid=0"
        },
        "columns": {
          "mappingMode": "autoMapInputData",
          "value": {},
          "matchingColumns": [
            "Competitor Name"
          ],
          "schema": [
            {
              "id": "Competitor Name",
              "displayName": "Competitor Name",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Website URL",
              "displayName": "Website URL",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Research",
              "displayName": "Research",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "23-07-2025",
              "displayName": "23-07-2025",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "number",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {
          "handlingExtraData": "insertInNewColumn"
        }
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.6,
      "position": [
        1660,
        -40
      ],
      "id": "af730b39-6074-4a80-bf51-d5efb0220a98",
      "name": "Update row in sheet",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "3WUfENHi9FEtJRGR",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "fb507391-77ba-466c-b30c-02e8f875ff82",
              "name": "Competitor Name",
              "value": "={{ $('Get row(s) in sheet').item.json['Competitor Name'] }}",
              "type": "string"
            },
            {
              "id": "e0b8c576-f151-4773-af39-4f831927115a",
              "name": "={{ $now.format('dd-MM-yyyy') }}",
              "value": "={{ $json.text }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        1320,
        -40
      ],
      "id": "357fcf64-6a40-4991-8cc4-74bcd64d58b0",
      "name": "Edit Fields1"
    },
    {
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "weeks",
              "triggerAtDay": [
                1
              ],
              "triggerAtHour": 9
            }
          ]
        }
      },
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.2,
      "position": [
        -340,
        -80
      ],
      "id": "6f28d3d4-a665-4334-afed-1389dec11e5a",
      "name": "Schedule Trigger1"
    }
  ],
  "connections": {
    "When clicking ‘Execute workflow’": {
      "main": [
        [
          {
            "node": "Get row(s) in sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get row(s) in sheet": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          },
          {
            "node": "HTTP Request1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request1": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Merge": {
      "main": [
        [
          {
            "node": "Edit Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Edit Fields": {
      "main": [
        [
          {
            "node": "Basic LLM Chain",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Basic LLM Chain": {
      "main": [
        [
          {
            "node": "Edit Fields1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Basic LLM Chain",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Edit Fields1": {
      "main": [
        [
          {
            "node": "Update row in sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Schedule Trigger1": {
      "main": [
        [
          {
            "node": "Get row(s) in sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "b79a93314bb2f206e41476559334e8cdfdb980a7d5e63d18255db0b669557266"
  }
}
