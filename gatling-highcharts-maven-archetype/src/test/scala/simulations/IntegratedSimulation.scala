package simulations

import io.gatling.core.Predef._
import io.gatling.core.scenario.Simulation
import io.gatling.http.Predef._

import java.time.LocalDateTime

class IntegratedSimulation extends Simulation {

  val bookingBaseUrl = URLConstants.booking_service
  val menuBaseUrl = URLConstants.menu_service
  val billingBaseUrl = URLConstants.billing_service
//
//  val bookingServiceConf = http.baseUrl(bookingBaseUrl)
//    .header("Accept", value = "application/json")
//    .header("content-type", value = "application/json")

  val menuServiceConf = http.baseUrl(menuBaseUrl)
    .header("Accept", value = "application/json")
    .header("content-type", value = "application/json")

//  val billingServiceConf = http.baseUrl(billingBaseUrl)
//    .header("Accept", value = "application/json")
//    .header("content-type", value = "application/json")

  val time = LocalDateTime.now()
  val feeder = csv("./src/test/scala/simulations/user_ids.csv").circular

  val fullCycleWoBookingScenario = scenario(scenarioName = "full cycle without booking")
    .exec(http(requestName = "get menu details")
      .get("getMenuItems")
      .check(status is 200))

    .pause(duration = 1)

    .feed(feeder)

    .exec(http(requestName = "get menu details")
      .get("getMenuItems?user_id=#{user_id}")
      .check(status is 200))

//    .exec(http(requestName = "take order")
//      .post("takeOrder")
//      .body(StringBody(s"\"{\\n    \\\"user_id\\\": \\\"${time}\\\",\\n " +
//        s"   \\\"order_list\\\": [\\n        {\\n            \\\"id\\\": 1,\\n" +
//        s"            \\\"qty\\\": 40\\n        },\\n        {\\n            " +
//        s"\\\"id\\\": 2,\\n            \\\"qty\\\": 6\\n        }\\n    ],\\n" +
//        s"    \\\"has_booked\\\": false\\n}\""))
//      .check(status is 200))

//    .pause(duration = 1)
//
//    .exec(http(requestName = "get bill")
//      .get(s"${URLConstants.billing_service}bill")
//      .queryParam("user_id", s"${time}")
//      .check(status is 200))
//
//    .pause(duration = 1)
//
//    .exec(http("pay bill")
//      .get(s"${URLConstants.billing_service}pay")
//      .queryParam("user_id", s"${time}")
//      .check(status is 200))

  setUp(fullCycleWoBookingScenario.inject(atOnceUsers(1))).protocols(menuServiceConf)
}