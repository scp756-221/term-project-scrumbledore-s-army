package simulations

import io.gatling.core.Predef._
import io.gatling.core.scenario.Simulation
import io.gatling.http.Predef._

class BookingIntegratedSimulation extends Simulation {

  val bookingBaseUrl = URLConstants.booking_service
  val menuBaseUrl = URLConstants.menu_service
  val billingBaseUrl = URLConstants.billing_service

  val menuServiceConf = http.baseUrl(menuBaseUrl)
    .header("Accept", value = "application/json")
    .header("content-type", value = "application/json")

  val feeder = csv("users.csv").circular

  val fullCycleWoBookingScenario = scenario(scenarioName = "full cycle with booking")

    .feed(feeder)

    .exec(http(requestName = "make booking")
      .get(s"${URLConstants.booking_service}book")
      .queryParam("booking_id", "${Number}")
      .check(status in (200, 422)))

    .pause(duration = 1)

    .exec(http("get booking")
      .get(s"${URLConstants.booking_service}get_booking")
      .queryParam("booking_id", "${Number}")
      .check(status.saveAs("bookingStatus"))
      .check(status in (200, 422)))

    .doIf(session => session("bookingStatus").as[String].equals("200")) {
      exec(http(requestName = "get menu details")
        .get("getMenuItems")
        .check(status is 200))

      .pause(duration = 1)

      .exec(http(requestName = "take order")
        .post("takeOrder")
        .body(StringBody("\"{\\n    \\\"user_id\\\": \\\"${ID}\\\",\\n    \\\"order_list\\\": [\\n        {\\n            \\\"id\\\": 1,\\n            \\\"qty\\\": 2\\n        },\\n        {\\n            \\\"id\\\": 2,\\n            \\\"qty\\\": 5\\n        }\\n    ],\\n    \\\"has_booked\\\": true\\n}\""))
        .check(status in (200)))

      .pause(duration = 1)

      .exec(http(requestName = "get bill")
        .get(s"${URLConstants.billing_service}bill")
        .queryParam("user_id", "${ID}")
        .check(status in(200, 422)))

      .pause(duration = 1)

      .exec(http("pay bill")
        .get(s"${URLConstants.billing_service}pay")
        .queryParam("user_id", "${ID}")
        .queryParam("booking_id", "${Number}")
        .check(status in(200, 422, 409)))

    }

  setUp(fullCycleWoBookingScenario.inject(atOnceUsers(5))).protocols(menuServiceConf)
}