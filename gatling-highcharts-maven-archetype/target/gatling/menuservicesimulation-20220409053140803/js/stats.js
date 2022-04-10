var stats = {
    type: "GROUP",
name: "Global Information",
path: "",
pathFormatted: "group_missing-name-b06d1",
stats: {
    "name": "Global Information",
    "numberOfRequests": {
        "total": "4",
        "ok": "4",
        "ko": "0"
    },
    "minResponseTime": {
        "total": "2718",
        "ok": "2718",
        "ko": "-"
    },
    "maxResponseTime": {
        "total": "7344",
        "ok": "7344",
        "ko": "-"
    },
    "meanResponseTime": {
        "total": "4984",
        "ok": "4984",
        "ko": "-"
    },
    "standardDeviation": {
        "total": "2267",
        "ok": "2267",
        "ko": "-"
    },
    "percentiles1": {
        "total": "4938",
        "ok": "4938",
        "ko": "-"
    },
    "percentiles2": {
        "total": "7204",
        "ok": "7204",
        "ko": "-"
    },
    "percentiles3": {
        "total": "7316",
        "ok": "7316",
        "ko": "-"
    },
    "percentiles4": {
        "total": "7338",
        "ok": "7338",
        "ko": "-"
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
    "count": 4,
    "percentage": 100
},
    "group4": {
    "name": "failed",
    "count": 0,
    "percentage": 0
},
    "meanNumberOfRequestsPerSecond": {
        "total": "0.308",
        "ok": "0.308",
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
        "total": "2",
        "ok": "2",
        "ko": "0"
    },
    "minResponseTime": {
        "total": "2718",
        "ok": "2718",
        "ko": "-"
    },
    "maxResponseTime": {
        "total": "2718",
        "ok": "2718",
        "ko": "-"
    },
    "meanResponseTime": {
        "total": "2718",
        "ok": "2718",
        "ko": "-"
    },
    "standardDeviation": {
        "total": "0",
        "ok": "0",
        "ko": "-"
    },
    "percentiles1": {
        "total": "2718",
        "ok": "2718",
        "ko": "-"
    },
    "percentiles2": {
        "total": "2718",
        "ok": "2718",
        "ko": "-"
    },
    "percentiles3": {
        "total": "2718",
        "ok": "2718",
        "ko": "-"
    },
    "percentiles4": {
        "total": "2718",
        "ok": "2718",
        "ko": "-"
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
    "count": 2,
    "percentage": 100
},
    "group4": {
    "name": "failed",
    "count": 0,
    "percentage": 0
},
    "meanNumberOfRequestsPerSecond": {
        "total": "0.154",
        "ok": "0.154",
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
        "ok": "2",
        "ko": "0"
    },
    "minResponseTime": {
        "total": "7157",
        "ok": "7157",
        "ko": "-"
    },
    "maxResponseTime": {
        "total": "7344",
        "ok": "7344",
        "ko": "-"
    },
    "meanResponseTime": {
        "total": "7251",
        "ok": "7251",
        "ko": "-"
    },
    "standardDeviation": {
        "total": "94",
        "ok": "94",
        "ko": "-"
    },
    "percentiles1": {
        "total": "7251",
        "ok": "7251",
        "ko": "-"
    },
    "percentiles2": {
        "total": "7297",
        "ok": "7297",
        "ko": "-"
    },
    "percentiles3": {
        "total": "7335",
        "ok": "7335",
        "ko": "-"
    },
    "percentiles4": {
        "total": "7342",
        "ok": "7342",
        "ko": "-"
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
    "count": 2,
    "percentage": 100
},
    "group4": {
    "name": "failed",
    "count": 0,
    "percentage": 0
},
    "meanNumberOfRequestsPerSecond": {
        "total": "0.154",
        "ok": "0.154",
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
