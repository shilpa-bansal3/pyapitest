class Schemas():
    """ Class to store all json schema definitions """

    schema_all = {
        "type": "object",
        "properties": {
            "RestResponse": {
                "type": "object",
                "properties": {
                    "messages": {
                        "type": "array",
                        "items": [
                            {"type": "string"}
                        ]
                    },
                    "result": {
                        "type": "array",
                        "items": [
                            {"type": "object",
                             "properties": {
                                 "name": {
                                     "type": "string"
                                 },
                                 "alpha2_code": {
                                     "type": "string"
                                 },
                                 "alpha3_code": {
                                     "type": "string"
                                 }
                             },
                             "required": [
                                 "name",
                                 "alpha2_code",
                                 "alpha3_code"
                             ]
                             },
                        ]
                    }
                },
                "required": [
                    "messages",
                    "result"
                ]
            }
        },
        "required": [
            "RestResponse"
        ]
    }


    schema_iso = {
        "type": "object",
          "properties": {
            "RestResponse": {
              "type": "object",
              "properties": {
                "messages": {
                  "type": "array",
                  "items": [
                    { "type": "string" }
                  ]
                },
                "result": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string"
                    },
                    "alpha2_code": {
                      "type": "string"
                    },
                    "alpha3_code": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "name",
                    "alpha2_code",
                    "alpha3_code"
                  ]
                }
              },
              "required": [
                "messages",
                "result"
              ]
            }
          },
          "required": [
            "RestResponse"
          ]
        }


    schema_iso_invalid = {
          "type": "object",
          "properties": {
            "RestResponse": {
              "type": "object",
              "properties": {
                "messages": {
                  "type": "array",
                  "items": [
                    {
                      "type": "string"
                    }
                  ]
                }
              },
              "required": [
                "messages"
              ]
            }
          },
          "required": [
            "RestResponse"
          ]
        }

    schema_search_invalid = {
          "type": "object",
          "properties": {
            "RestResponse": {
              "type": "object",
              "properties": {
                "messages": {
                  "type": "array",
                  "items": [
                    {
                      "type": "string"
                    }
                  ]
                },
                "result": {
                  "type": "array",
                  "items": {}
                }
              },
              "required": [
                "messages",
                "result"
              ]
            }
          },
          "required": [
            "RestResponse"
          ]
        }