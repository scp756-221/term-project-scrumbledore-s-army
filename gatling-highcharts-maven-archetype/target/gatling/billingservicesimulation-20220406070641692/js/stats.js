var stats = {
    type: "GROUP",
name: "Global Information",
path: "",
pathFormatted: "group_missing-name-b06d1",
stats: {
    "name": "Global Information",
    "numberOfRequests": {
        "total": "2",
        "ok": "0",
        "ko": "2"
    },
    "minResponseTime": {
        "total": "10007",
        "ok": "-",
        "ko": "10007"
    },
    "maxResponseTime": {
        "total": "10009",
        "ok": "-",
        "ko": "10009"
    },
    "meanResponseTime": {
        "total": "10008",
        "ok": "-",
        "ko": "10008"
    },
    "standardDeviation": {
        "total": "1",
        "ok": "-",
        "ko": "1"
    },
    "percentiles1": {
        "total": "10008",
        "ok": "-",
        "ko": "10008"
    },
    "percentiles2": {
        "total": "10009",
        "ok": "-",
        "ko": "10009"
    },
    "percentiles3": {
        "total": "10009",
        "ok": "-",
        "ko": "10009"
    },
    "percentiles4": {
        "total": "10009",
        "ok": "-",
        "ko": "10009"
    },
    "group1": {
    "name": "t < 800 ms",
    "count": 0,
    "percentage": 0
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
    "count": 2,
    "percentage": 100
},
    "meanNumberOfRequestsPerSecond": {
        "total": "0.083",
        "ok": "-",
        "ko": "0.083"
    }
},
contents: {
"req_get-bill-1ce4d": {
        type: "REQUEST",
        name: "get bill",
path: "get bill",
pathFormatted: "req_get-bill-1ce4d",
stats: {
    "name": "get bill",
    "numberOfRequests": {
        "total": "1",
        "ok": "0",
        "ko": "1"
    },
    "minResponseTime": {
        "total": "10007",
        "ok": "-",
        "ko": "10007"
    },
    "maxResponseTime": {
        "total": "10007",
        "ok": "-",
        "ko": "10007"
    },
    "meanResponseTime": {
        "total": "10007",
        "ok": "-",
        "ko": "10007"
    },
    "standardDeviation": {
        "total": "0",
        "ok": "-",
        "ko": "0"
    },
    "percentiles1": {
        "total": "10007",
        "ok": "-",
        "ko": "10007"
    },
    "percentiles2": {
        "total": "10007",
        "ok": "-",
        "ko": "10007"
    },
    "percentiles3": {
        "total": "10007",
        "ok": "-",
        "ko": "10007"
    },
    "percentiles4": {
        "total": "10007",
        "ok": "-",
        "ko": "10007"
    },
    "group1": {
    "name": "t < 800 ms",
    "count": 0,
    "percentage": 0
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
    "count": 1,
    "percentage": 100
},
    "meanNumberOfRequestsPerSecond": {
        "total": "0.042",
        "ok": "-",
        "ko": "0.042"
    }
}
    },"req_pay-bill-8327e": {
        type: "REQUEST",
        name: "pay bill",
path: "pay bill",
pathFormatted: "req_pay-bill-8327e",
stats: {
    "name": "pay bill",
    "numberOfRequests": {
        "total": "1",
        "ok": "0",
        "ko": "1"
    },
    "minResponseTime": {
        "total": "10009",
        "ok": "-",
        "ko": "10009"
    },
    "maxResponseTime": {
        "total": "10009",
        "ok": "-",
        "ko": "10009"
    },
    "meanResponseTime": {
        "total": "10009",
        "ok": "-",
        "ko": "10009"
    },
    "standardDeviation": {
        "total": "0",
        "ok": "-",
        "ko": "0"
    },
    "percentiles1": {
        "total": "10009",
        "ok": "-",
        "ko": "10009"
    },
    "percentiles2": {
        "total": "10009",
        "ok": "-",
        "ko": "10009"
    },
    "percentiles3": {
        "total": "10009",
        "ok": "-",
        "ko": "10009"
    },
    "percentiles4": {
        "total": "10009",
        "ok": "-",
        "ko": "10009"
    },
    "group1": {
    "name": "t < 800 ms",
    "count": 0,
    "percentage": 0
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
    "count": 1,
    "percentage": 100
},
    "meanNumberOfRequestsPerSecond": {
        "total": "0.042",
        "ok": "-",
        "ko": "0.042"
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
