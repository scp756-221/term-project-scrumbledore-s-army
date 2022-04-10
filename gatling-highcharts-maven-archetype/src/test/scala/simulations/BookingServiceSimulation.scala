package simulations

import io.gatling.core.Predef._
import io.gatling.core.scenario.Simulation
import io.gatling.http.Predef._

class BookingServiceSimulation extends Simulation {

  val baseUrl = URLConstants.booking_service

  val bookingServiceConf = http.baseUrl(baseUrl)
    .header("Accept", value = "application/json")
    .header("content-type", value = "application/json")

  val bookScenario = scenario(scenarioName = "make booking")
    .exec(http(requestName = "make booking")
      .get("book")
      .queryParam("booking_id", "2234567890")
      .check(status is 200))

    .pause(duration = 2)

    .exec(http("get booking")
      .get("get_booking")
      .queryParam("booking_id", "2234567890")
      .check(status is 200))

  setUp(bookScenario.inject(atOnceUsers(1))).protocols(bookingServiceConf)

}
