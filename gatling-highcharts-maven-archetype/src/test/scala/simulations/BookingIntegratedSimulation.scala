package simulations

import io.gatling.core.Predef._
import io.gatling.core.scenario.Simulation
import io.gatling.http.Predef._

import java.time.LocalDateTime

class BookingIntegratedSimulation extends Simulation {

  val bookingBaseUrl = URLConstants.booking_service
  val menuBaseUrl = URLConstants.menu_service
  val billingBaseUrl = URLConstants.billing_service

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
  val feeder = csv("/Users/anchal/Downloads/test/gatling-highcharts-maven-archetype/src/test/scala/simulations/users.csv").circular

  val fullCycleWoBookingScenario = scenario(scenarioName = "full cycle with booking")

    .exec(http(requestName = "make booking")
      .get(s"${URLConstants.booking_service}book")
      .queryParam("booking_id", "2234567890")
      .check(status in (200, 422)))

    .pause(duration = 2)

    .exec(http("get booking")
      .get(s"${URLConstants.booking_service}get_booking")
      .queryParam("booking_id", "2234567890")
      .check(status is 200))

    .exec(http(requestName = "get menu details")
      .get("getMenuItems")
      .check(status is 200))

    .pause(duration = 1)

    .feed(feeder)

    .exec(http(requestName = "take order")
      .post("takeOrder")
      .body(StringBody(s"\"{\\n    \\\"user_id\\\": \\\"${time}\\\",\\n " +
        s"   \\\"order_list\\\": [\\n        {\\n            \\\"id\\\": 1,\\n" +
        s"            \\\"qty\\\": 40\\n        },\\n        {\\n            " +
        s"\\\"id\\\": 2,\\n            \\\"qty\\\": 6\\n        }\\n    ],\\n" +
        s"    \\\"has_booked\\\": true\\n}\""))
      .check(status in (200, 500)))

    .pause(duration = 1)

    .exec(http(requestName = "get bill")
      .get(s"${URLConstants.billing_service}bill")
      .queryParam("user_id", s"${time}")
      .check(status is 200))

    .pause(duration = 1)

    .exec(http("pay bill")
      .get(s"${URLConstants.billing_service}pay")
      .queryParam("user_id", s"${time}")
      .queryParam("booking_id", "2234567890")
      .check(status in (200, 422, 409)))

  setUp(fullCycleWoBookingScenario.inject(atOnceUsers(1))).protocols(menuServiceConf)
}