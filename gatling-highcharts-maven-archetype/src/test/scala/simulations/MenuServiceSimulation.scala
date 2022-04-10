package simulations

import io.gatling.core.Predef._
import io.gatling.core.scenario.Simulation
import io.gatling.http.Predef._

import java.time.LocalDateTime

class MenuServiceSimulation extends Simulation {

  val baseUrl = URLConstants.menu_service
//  val pathToBody = "./src/test/resources/json_bodies/menu_service"


  val menuServiceConf = http.baseUrl(baseUrl)
    .header("Accept", value="application/json")
    .header("content-type", value="application/json")

  val getMenuScenario = scenario(scenarioName = "get menu")
    .exec(http(requestName = "get menu details")
      .get("getMenuItems")
      .check(status is 200))

//  setUp(getMenuScenario.inject(atOnceUsers(100))).protocols(menuServiceConf)

  val takeOrderScenario = scenario(scenarioName = "take order")
    .exec(http(requestName = "take order")
      .post("takeOrder")
      .body(StringBody("\"{\\n    \\\"user_id\\\": \\\"202204-0517-0226-649b29ee-2861-4caf-9362-7aee2c054f85\\\",\\n    \\\"order_list\\\": [\\n        {\\n            \\\"id\\\": 1,\\n            \\\"qty\\\": 2\\n        },\\n        {\\n            \\\"id\\\": 2,\\n            \\\"qty\\\": 5\\n        }\\n    ],\\n    \\\"has_booked\\\": false\\n}\""))
      .check(status is 200))

//  setUp(takeOrderScenario.inject(atOnceUsers(1))).protocols(menuServiceConf)

  val time = LocalDateTime.now()

  val menuWithOrderScenario = scenario(scenarioName = "get menu")
    .exec(http(requestName = "get menu details")
      .get("getMenuItems")
      .check(status is 200))

    .pause(duration = 2)

    .exec(http(requestName = "take order")
      .post("takeOrder")
      .body(StringBody(s"\"{\\n    \\\"user_id\\\": \\\"${time}\\\",\\n    \\\"order_list\\\": [\\n        {\\n            \\\"id\\\": 1,\\n            \\\"qty\\\": 2\\n        },\\n        {\\n            \\\"id\\\": 2,\\n            \\\"qty\\\": 5\\n        }\\n    ],\\n    \\\"has_booked\\\": false\\n}\""))
      .check(status is 200))

  setUp(menuWithOrderScenario.inject(atOnceUsers(2))).protocols(menuServiceConf)

}