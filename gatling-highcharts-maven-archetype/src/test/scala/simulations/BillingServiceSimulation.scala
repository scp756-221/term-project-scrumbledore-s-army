package simulations

import io.gatling.core.Predef._
import io.gatling.core.scenario.Simulation
import io.gatling.http.Predef._

class BillingServiceSimulation extends Simulation {

  val baseUrl = URLConstants.billing_service

  val billingServiceConf = http.baseUrl(baseUrl)
    .header("Accept", value="application/json")
    .header("content-type", value="application/json")

  val billScenario = scenario(scenarioName = "bill payment")
    .exec(http(requestName = "get bill")
      .get("bill")
      .queryParam("user_id", "#{user_id}")
      .check(status is 200))

    .pause(duration = 1)

    .exec(http("pay bill")
      .get("pay")
      .queryParam("user_id", "#{user_id}")
//      .queryParam("booking_id", None)
      .check(status is 200))

  setUp(billScenario.inject(atOnceUsers(1))).protocols(billingServiceConf)

}