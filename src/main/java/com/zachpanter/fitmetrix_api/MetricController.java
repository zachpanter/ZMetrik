package com.zachpanter.fitmetrix_api;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MetricController {

    SQLiteService sqliteService;
    
    @PostMapping("/addSet")
    public void addSet( @RequestParam(value="liftTitle") String liftTitle,
                        @RequestParam(value="weight") Integer weight, 
                        @RequestParam(value="reps") Integer reps) {
        sqliteService.addSet(liftTitle, weight, reps);
    }

    @GetMapping("/getOneRepMax")
    public Integer getOneRepMax(@RequestParam(value="title") String title) {
        return sqliteService.getCurrentOneRepMax(title);
    }

    // TODO: Implement for daily stats
    // @GetMapping("/getTodaysVolumeForLift")
    // public Integer getTodaysVolumeForLift(@RequestParam(value="title") String title) {
    //     return sqliteService.getTodaysVolumeForLift(title); 
    // }

    // TODO: Implement for weekly stats
    // @GetMapping("/getWeeksVolumeForLift")
    // public Integer getWeeksVolumeForLift(@RequestParam(value="title") String title) {
    //     return sqliteService.getWeeksVolumeForLift(title);  
    // }

}