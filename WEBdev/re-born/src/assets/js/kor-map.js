var widthFull = 800,
    aspectRatio = 1,
    mapMargin = {left: 10, right: 10, top: 10, bottom: 10},
    defOpacity = 0.5,
    defStrokewidth = 2;
var ctprvnDiv = d3.select("#ctprvn-nm"),
    sigDiv = d3.select("#sig-nm"),
    emdDiv = d3.select("#emd-nm");
var mainSvg = d3.select("#main-map")
        .append("svg")
        .attr("width", widthFull)
        .attr("height", aspectRatio*widthFull)
        .attr("viewBox", "15,0," + widthFull + "," + widthFull*aspectRatio)
        .attr("preserveAspectRatio", "xMinYMin meet")
        .classed("svg-content-responsive", true),
    map = mainSvg.append("g"),
    ocean = map.append("rect")
        .attr("width", widthFull)
        .attr("height", aspectRatio*widthFull)
        .attr("class", "ocean"),
    color = d3.scaleOrdinal(d3.schemeCategory10);
    zoom = d3.zoom()
       .scaleExtent([1, 5])
       .translateExtent([[0,0],[widthFull, widthFull*aspectRatio]]),
    currTransform = [0,0],
    initScale = 1;


// get containing box dimension
function getCurrDim() {
    return d3.select(".map-container")
        .node()
        .getBoundingClientRect();
}
// Select the tooltip div
var tooltip = d3.select("body")
        .append("div")
        .attr("id", "tooltip")
        .style("opacity", 0);
​
// Back button
var back = mainSvg.append("g")
        .classed("back-button", true)
        .attr("transform", "translate(20,20)")
        .style("opacity", 1);
back.append("polyline")
    .attr("points", "0,18 9,0 18,18");
var backText = back.append("text")
        .attr("x", 30)
        .attr("y", 20);
​
// Read level 1 map data
d3.json('/static/maps/assets/data/plot/kor_admin_1.topojson').then(function(data1){
​
    // var selectarea = document.getElementById("SelectArea")
    // var selectsigungu = document.getElementById("SelectSigungu")
    // var target = document.getElementById("observe")
    // var latlon = document.getElementById("latlon")
​
    var lvl1 = topojson.feature(data1, data1.objects.TL_SCCO_CTPRVN),
        lvl2, lvl3,
        projection = d3.geoNaturalEarth1(),
        path = d3.geoPath()
            .projection(projection);
    lvl1.features.forEach(function(d) { d.id = d.properties.CTPRVN_CD; });
​
    // reusuable draw function
    function redraw(selected) {
        var currDim = getCurrDim();
        // hide tooltip
        tooltip.transition()
            .duration(200)
            .style("opacity", 1);
        // refit projection
        projection.fitExtent([
            [mapMargin.left,mapMargin.top],
            [currDim.width - mapMargin.right, currDim.height - mapMargin.bottom]
        ], selected);
        // reset zoom
        mainSvg.transition().duration(750).call(zoom.transform, d3.zoomIdentity);
        initTranslate = projection.translate(),
        initScale = projection.scale();
        // redraw map
        var area = map.selectAll(".area")
                .data(selected.features, function(d) { return d.id; })
        area.exit().remove();
        area.enter().append("path")
            .attr("class", "area")
            .on("mouseover", mouseoverHandler)
            .on("mouseout", mouseoutHandler)
            .on("click", clickHandler)
            .attr("d", path)
            .attr("fill", function(s, i) {
                return (s.properties.LVL_1_EN==null)?"#ff0000":color(1);
            })
            .style("fill-opacity", defOpacity);
    }
    redraw(lvl1);
​
    // Read level 2 map data
    d3.json('/static/maps/assets/data/plot/kor_admin_2.topojson').then(function(data2){
        // Read level 3 map data
        d3.json('/static/maps/assets/data/plot/kor_admin_3.topojson').then(function(data3){
            lvl2 = topojson.feature(data2, data2.objects.TL_SCCO_SIG),
            lvl3 = topojson.feature(data3, data3.objects.TL_SCCO_EMD);
            lvl2.features.forEach(function(d) { d.id = d.properties.LVL_2_KR; });
            lvl3.features.forEach(function(d) { d.id = d.properties.LVL_3_KR; });
        });
    });
​
    // mouse interaction handlers
    back
        .on("mouseover", function(){
            if(currRegion.length > 0) { d3.select(this).style("opacity", 1); }
        })
        .on("mouseout", function(){
            if(currRegion.length > 0) { d3.select(this).style("opacity", defOpacity); }
        })
        .on("click", clickoutHandler);
    ocean.on("click", clickoutHandler);
    var currRegion = [];
    function clickHandler(d) {
        switch(currRegion.length){
            case 0:
                currRegion = [{key: "LVL_1_KR", value: d.properties.LVL_1_KR}];
                backText.text("전국지도");
                back.style("opacity", defOpacity);
                
                // 지도(지역) 클릭 시 리스트(지역) 변경
                // wrap = document.getElementById('wrapSelect')
                // area = document.getElementById('region')
                // for (var i = 0; i < area.length; i++) {
                //     if (area.options[i].innerText === d.properties.LVL_1_KR) {
                //         area.options[i].selected = true;
                //         area.dispatchEvent(new Event('change'))
                //         break
                //     }
                // }
​
                // if(d.properties.LVL_1_EN=="Sejong"){
                //     sigungu.disabled = true;
                //     clickHandler(filterGeo(lvl2, currRegion).features[0]);
                //     break;
                // } else {
                //     redraw(filterGeo(lvl2, currRegion));
                //     break;
                // }
​
            case 1:
                if(d.properties.LVL_1_EN!="Sejong"){
                    backText.text(d.properties.LVL_1_KR + " 지도");
                }
                currRegion = [
                    {key: "LVL_1_EN", value: d.properties.LVL_1_EN},
                    {key: "LVL_2_EN", value: d.properties.LVL_2_EN}
                ];
                redraw(filterGeo(lvl3, currRegion));
​
                // 지도(시군구) 클릭 시 리스트 시군구 변경
                // sigungu = document.getElementById('sigungu')
                // for (var i = 0; i < sigungu.length; i++) {
                //     if (sigungu.options[i].innerText === d.properties.LVL_2_KR) {
                //         sigungu.value = sigungu.options[i].value
                //         sigungu.dispatchEvent(new Event('change'))
                //         break
                //     }
                // }
                break;
            case 2:
                break;
            default:
                throw "unreachable";
        }
    }
    function clickoutHandler() {
        switch(currRegion.length){
            case 2:
                currRegion.pop();
                if(currRegion[0].value=="Sejong"){
                    clickoutHandler();
                    break;
                } else {
                    // sigungu.click()
                    backText.text("전국지도");
                    sigDiv.html("");
                    redraw(filterGeo(lvl2, currRegion));
                    break;
                }
            case 1:
                area.value = "all"
                // sigungu.disabled = false;
                area.click()
                back.style("opacity", 0);
                ctprvnDiv.html("");
                currRegion = [];
                redraw(lvl1);
                break;
            case 0:
                break;
            default:
                throw "unreachable";
        }
    }
    function mouseoverHandler(d) {
        // display selected region name
        var tooltipText = d.properties.LVL_1_KR + "<br />" + d.properties.LVL_1_EN;
        ctprvnDiv.html(tooltipText);
        if(currRegion.length>0) {
            tooltipText = d.properties.LVL_2_KR + "<br />" + d.properties.LVL_2_EN;
            sigDiv.html(tooltipText);
        }
        if(currRegion.length>1) {
            tooltipText = d.properties.EMD_KOR_NM + "<br/>" + d.properties.EMD_ENG_NM;
            emdDiv.html(tooltipText);
        }
        tooltip.html(tooltipText);
        tooltip
            .style("left", (d3.event.pageX) + "px")
            .style("top", (d3.event.pageY - 40) + "px")
            .raise()
            .transition()
            .duration(200)
            .style("opacity", 0.9);
        // highlight selected region
        d3.select(this).raise();
        d3.select(this)
            .style("stroke-width", 0)
            .style("fill-opacity", 1);
    }
    function mouseoutHandler(d) {
        if(currRegion.length<1) { ctprvnDiv.html(""); }
        if(currRegion.length<2) { sigDiv.html(""); }
        emdDiv.html("");
        tooltip.transition()
            .duration(200)
            .style("opacity", 0);
        d3.select(this)
            .style("stroke-width", defStrokewidth)
            .style("fill-opacity", defOpacity);
    }
    // enable zooming
    function zoomed() {
        var newScale = initScale * d3.event.transform.k;
        projection
            .translate([
                (initTranslate[0] * d3.event.transform.k) + d3.event.transform.x,
                (initTranslate[1] * d3.event.transform.k) + d3.event.transform.y
            ])
            .scale(newScale);
        map.selectAll("path").attr("d", path);
    }
​
    // resize on window
    window.addEventListener("resize", function(){
        switch(currRegion.length){
            case 0:
                redraw(lvl1);
                break;
            case 1:
                redraw(filterGeo(lvl2, currRegion));
                break;
            case 2:
                redraw(filterGeo(lvl3, currRegion));
                break;
            default:
                throw "unreachable";
        }
    });
​
​
    // 리스트 클릭시 지도 따라 움직이기
    // MutationObserver => target으로 설정한 DOM을 감시하는 함수! config에서 true로 설정한 값이 변경될 시 감지한다.
    // var config = { characterData: true, subtree: true, childList: true, attributes: true, oldchildList: true }
​
    // var MutationObserver = window.MutationObserver || window.WebKitMutationObserver;
​
    // var divObserver = new MutationObserver(function() {})
​
    // 지역 고르면 지역 이동
    // var areaObserver = new MutationObserver(function(mutations) {
        // if (selectarea.innerText === "전체보기") {
            // currRegion = []
            // redraw(lvl1)
        // } else {
            // currRegion = [{key: "LVL_1_KR", value: selectarea.innerText}]
            // redraw(filterGeo(lvl2, currRegion))
        // }
    // })
    // 시군구 고르면 시군구 이동
    // var sigunguObserver = new MutationObserver(function() {
    //     currRegion = [
    //         {key: "LVL_1_KR", value: selectarea.innerText},
    //         {key: "LVL_2_KR", value: selectsigungu.innerText}
    //     ]
​
    //     redraw(filterGeo(lvl3, currRegion))
    // })
​
    // var latlonObserver = new MutationObserver(function(mutations) {
    //     var cate = ""
    //     mutations.forEach(function(mutation) {
    //         if (mutation.type == "attributes") {
    //             cate = mutation['target']['name']
​
    //             if (document.getElementById(`check_${cate}`).checked == false) {
                    
    //                 mainSvg.selectAll("svg > image")['_groups'][0].forEach(function(item) {
    //                     console.log(item.getAttribute('category'))
    //                     if (item.getAttribute('category') == cate) {
    //                         item.remove()
    //                     }
    //                 })
​
    //             }
​
    //         } else if (mutation.type == "childList") {
    //             if (mutation['addedNodes'].length > 0) {
    //                 mutation['addedNodes'].forEach(function(item) {
    //                     var mapxy = [item.value, item.innerText]
    
    //                     mainSvg.selectAll("svg")
    //                         .data([mapxy]).enter()
    //                         .append("svg:image")
    //                         .attr("category", cate)
    //                         .attr("width", 30)
    //                         .attr("height", 30)
    //                         .attr("id", mapxy[0])
    //                         .attr("x", (d)=>projection(d)[0])
    //                         .attr("y", (d)=>projection(d)[1])
    //                         .attr("xlink:href", "/static/maps/img/pin.svg")
    //                 })
    //             }
                
    //             if (mutation['removedNodes'].length > 0) {
    //                 mutation['removedNodes'].forEach(function(item) {
    //                     var mapxy = [item.value, item.innerText]
                        
    //                     mainSvg.selectAll("svg > image")['_groups'][0].forEach(function(image) {
    //                         if (image.id == item.value) {
    //                             image.remove()
    //                         }
    //                     })
    //                 })
    //             }
    //         }
    //     })
    // })
​
    // 실제 동작 감지 코드
    // Observer.observe(target, config) 형태로 사용
    // divObserver.observe(target, config)
    // areaObserver.observe(selectarea, config) 
    // sigunguObserver.observe(selectsigungu, config)
    // latlonObserver.observe(latlon, config)
​
});
​
// filter to focus on regions
function filterGeo(data, filter) {
    var res = {type: "FeatureCollection"};
​
    res.features = data.features.filter(function(d) {
        var b = 1;
        filter.forEach(function(f) {
            b = b & (d.properties[f.key]==f.value);
        });
        return b;
    });
    return res;
}
​
// toggle dark color theme
function toggleTheme() {
    if(d3.select("#k-map").classed("dark")){
        d3.select("#k-map").classed("dark", false);
        d3.select("#tooltip").classed("dark", false);
        defOpacity = 0.9;
        map.selectAll(".area").style("fill-opacity", defOpacity);
    } else {
        d3.select("#k-map").classed("dark", true);
        d3.select("#tooltip").classed("dark", true);
        defOpacity = 0.9;
        map.selectAll(".area").style("fill-opacity", defOpacity);
    }
}
​
​