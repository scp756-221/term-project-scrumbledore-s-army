var stats = {
    type: "GROUP",
name: "Global Information",
path: "",
pathFormatted: "group_missing-name-b06d1",
stats: {
    "name": "Global Information",
    "numberOfRequests": {
        "total": "2",
        "ok": "2",
        "ko": "0"
    },
    "minResponseTime": {
        "total": "64",
        "ok": "64",
        "ko": "-"
    },
    "maxResponseTime": {
        "total": "161",
        "ok": "161",
        "ko": "-"
    },
    "meanResponseTime": {
        "total": "113",
        "ok": "113",
        "ko": "-"
    },
    "standardDeviation": {
        "total": "49",
        "ok": "49",
        "ko": "-"
    },
    "percentiles1": {
        "total": "113",
        "ok": "113",
        "ko": "-"
    },
    "percentiles2": {
        "total": "137",
        "ok": "137",
        "ko": "-"
    },
    "percentiles3": {
        "total": "156",
        "ok": "156",
        "ko": "-"
    },
    "percentiles4": {
        "total": "160",
        "ok": "160",
        "ko": "-"
    },
    "group1": {
    "name": "t < 800 ms",
    "count": 2,
    "percentage": 100
},
    "group2": {
    "name": "800 ms < t < 1200 ms",
    "count": 0,
    "percentage": 0
},
    "group3": {
    "name": "t > 1200 ms",
    "count": 0,
    "percentage": 0
},
    "group4": {
    "name": "failed",
    "count": 0,
    "percentage": 0
},
    "meanNumberOfRequestsPerSecond": {
        "total": "0.667",
        "ok": "0.667",
        "ko": "-"
    }
},
contents: {
"req_get-menu-detail-abe69": {
        type: "REQUEST",
        name: "get menu details",
path: "get menu details",
pathFormatted: "req_get-menu-detail-abe69",
stats: {
    "name": "get menu details",
    "numberOfRequests": {
        "total": "1",
        "ok": "1",
        "ko": "0"
    },
    "minResponseTime": {
        "total": "64",
        "ok": "64",
        "ko": "-"
    },
    "maxResponseTime": {
        "total": "64",
        "ok": "64",
        "ko": "-"
    },
    "meanResponseTime": {
        "total": "64",
        "ok": "64",
        "ko": "-"
    },
    "standardDeviation": {
        "total": "0",
        "ok": "0",
        "ko": "-"
    },
    "percentiles1": {
        "total": "64",
        "ok": "64",
        "ko": "-"
    },
    "percentiles2": {
        "total": "64",
        "ok": "64",
        "ko": "-"
    },
    "percentiles3": {
        "total": "64",
        "ok": "64",
        "ko": "-"
    },
    "percentiles4": {
        "total": "64",
        "ok": "64",
        "ko": "-"
    },
    "group1": {
    "name": "t < 800 ms",
    "count": 1,
    "percentage": 100
},
    "group2": {
    "name": "800 ms < t < 1200 ms",
    "count": 0,
    "percentage": 0
},
    "group3": {
    "name": "t > 1200 ms",
    "count": 0,
    "percentage": 0
},
    "group4": {
    "name": "failed",
    "count": 0,
    "percentage": 0
},
    "meanNumberOfRequestsPerSecond": {
        "total": "0.333",
        "ok": "0.333",
        "ko": "-"
    }
}
    },"req_take-order-95a7f": {
        type: "REQUEST",
        name: "take order",
path: "take order",
pathFormatted: "req_take-order-95a7f",
stats: {
    "name": "take order",
    "numberOfRequests": {
        "total": "1",
        "ok": "1",
        "ko": "0"
    },
    "minResponseTime": {
        "total": "161",
        "ok": "161",
        "ko": "-"
    },
    "maxResponseTime": {
        "total": "161",
        "ok": "161",
        "ko": "-"
    },
    "meanResponseTime": {
        "total": "161",
        "ok": "161",
        "ko": "-"
    },
    "standardDeviation": {
        "total": "0",
        "ok": "0",
        "ko": "-"
    },
    "percentiles1": {
        "total": "161",
        "ok": "161",
        "ko": "-"
    },
    "percentiles2": {
        "total": "161",
        "ok": "161",
        "ko": "-"
    },
    "percentiles3": {
        "total": "161",
        "ok": "161",
        "ko": "-"
    },
    "percentiles4": {
        "total": "161",
        "ok": "161",
        "ko": "-"
    },
    "group1": {
    "name": "t < 800 ms",
    "count": 1,
    "percentage": 100
},
    "group2": {
    "name": "800 ms < t < 1200 ms",
    "count": 0,
    "percentage": 0
},
    "group3": {
    "name": "t > 1200 ms",
    "count": 0,
    "percentage": 0
},
    "group4": {
    "name": "failed",
    "count": 0,
    "percentage": 0
},
    "meanNumberOfRequestsPerSecond": {
        "total": "0.333",
        "ok": "0.333",
        "ko": "-"
    }
}
    }
}

}

function fillStats(stat){
    $("#numberOfRequests").append(stat.numberOfRequests.total);
    $("#numberOfRequestsOK").append(stat.numberOfRequests.ok);
    $("#numberOfRequestsKO").append(stat.numberOfRequests.ko);

    $("#minResponseTime").append(stat.minResponseTime.total);
    $("#minResponseTimeOK").append(stat.minResponseTime.ok);
    $("#minResponseTimeKO").append(stat.minResponseTime.ko);

    $("#maxResponseTime").append(stat.maxResponseTime.total);
    $("#maxResponseTimeOK").append(stat.maxResponseTime.ok);
    $("#maxResponseTimeKO").append(stat.maxResponseTime.ko);

    $("#meanResponseTime").append(stat.meanResponseTime.total);
    $("#meanResponseTimeOK").append(stat.meanResponseTime.ok);
    $("#meanResponseTimeKO").append(stat.meanResponseTime.ko);

    $("#standardDeviation").append(stat.standardDeviation.total);
    $("#standardDeviationOK").append(stat.standardDeviation.ok);
    $("#standardDeviationKO").append(stat.standardDeviation.ko);

    $("#percentiles1").append(stat.percentiles1.total);
    $("#percentiles1OK").append(stat.percentiles1.ok);
    $("#percentiles1KO").append(stat.percentiles1.ko);

    $("#percentiles2").append(stat.percentiles2.total);
    $("#percentiles2OK").append(stat.percentiles2.ok);
    $("#percentiles2KO").append(stat.percentiles2.ko);

    $("#percentiles3").append(stat.percentiles3.total);
    $("#percentiles3OK").append(stat.percentiles3.ok);
    $("#percentiles3KO").append(stat.percentiles3.ko);

    $("#percentiles4").append(stat.percentiles4.total);
    $("#percentiles4OK").append(stat.percentiles4.ok);
    $("#percentiles4KO").append(stat.percentiles4.ko);

    $("#meanNumberOfRequestsPerSecond").append(stat.meanNumberOfRequestsPerSecond.total);
    $("#meanNumberOfRequestsPerSecondOK").append(stat.meanNumberOfRequestsPerSecond.ok);
    $("#meanNumberOfRequestsPerSecondKO").append(stat.meanNumberOfRequestsPerSecond.ko);
}
