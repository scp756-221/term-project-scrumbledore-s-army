var stats = {
    type: "GROUP",
name: "Global Information",
path: "",
pathFormatted: "group_missing-name-b06d1",
stats: {
    "name": "Global Information",
    "numberOfRequests": {
        "total": "4",
        "ok": "2",
        "ko": "2"
    },
    "minResponseTime": {
        "total": "60",
        "ok": "236",
        "ko": "60"
    },
    "maxResponseTime": {
        "total": "242",
        "ok": "242",
        "ko": "61"
    },
    "meanResponseTime": {
        "total": "150",
        "ok": "239",
        "ko": "61"
    },
    "standardDeviation": {
        "total": "89",
        "ok": "3",
        "ko": "1"
    },
    "percentiles1": {
        "total": "149",
        "ok": "239",
        "ko": "61"
    },
    "percentiles2": {
        "total": "238",
        "ok": "241",
        "ko": "61"
    },
    "percentiles3": {
        "total": "241",
        "ok": "242",
        "ko": "61"
    },
    "percentiles4": {
        "total": "242",
        "ok": "242",
        "ko": "61"
    },
    "group1": {
    "name": "t < 800 ms",
    "count": 2,
    "percentage": 50
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
    "percentage": 50
},
    "meanNumberOfRequestsPerSecond": {
        "total": "2",
        "ok": "1",
        "ko": "1"
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
        "total": "2",
        "ok": "2",
        "ko": "0"
    },
    "minResponseTime": {
        "total": "236",
        "ok": "236",
        "ko": "-"
    },
    "maxResponseTime": {
        "total": "242",
        "ok": "242",
        "ko": "-"
    },
    "meanResponseTime": {
        "total": "239",
        "ok": "239",
        "ko": "-"
    },
    "standardDeviation": {
        "total": "3",
        "ok": "3",
        "ko": "-"
    },
    "percentiles1": {
        "total": "239",
        "ok": "239",
        "ko": "-"
    },
    "percentiles2": {
        "total": "241",
        "ok": "241",
        "ko": "-"
    },
    "percentiles3": {
        "total": "242",
        "ok": "242",
        "ko": "-"
    },
    "percentiles4": {
        "total": "242",
        "ok": "242",
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
        "total": "1",
        "ok": "1",
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
        "total": "2",
        "ok": "0",
        "ko": "2"
    },
    "minResponseTime": {
        "total": "60",
        "ok": "-",
        "ko": "60"
    },
    "maxResponseTime": {
        "total": "61",
        "ok": "-",
        "ko": "61"
    },
    "meanResponseTime": {
        "total": "61",
        "ok": "-",
        "ko": "61"
    },
    "standardDeviation": {
        "total": "1",
        "ok": "-",
        "ko": "1"
    },
    "percentiles1": {
        "total": "61",
        "ok": "-",
        "ko": "61"
    },
    "percentiles2": {
        "total": "61",
        "ok": "-",
        "ko": "61"
    },
    "percentiles3": {
        "total": "61",
        "ok": "-",
        "ko": "61"
    },
    "percentiles4": {
        "total": "61",
        "ok": "-",
        "ko": "61"
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
        "total": "1",
        "ok": "-",
        "ko": "1"
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
