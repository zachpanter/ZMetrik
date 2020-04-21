package com.zachpanter.fitmetrix_api;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.Map;

import org.springframework.stereotype.Service;

import org.sqlite.SQLiteDataSource;

@Service
public class SQLiteService {

    Set<String> liftSet = new HashSet<String>();

    public SQLiteService() {
        populateLiftSet();
    }

    @Deprecated
    public void populateLiftSet() {
        String sql = "SELECT title FROM lift;";
        
        try (
            Connection conn = this.connect();
            Statement stmt = conn.createStatement();
            ResultSet resultSet = stmt.executeQuery(sql);
        ) {
            while (resultSet.next()) {
                liftSet.add(resultSet.getString("title"));
            }
        } catch (Exception ex) {
            System.out.println("There was an error");
        }

    }

    public Connection connect() {

        String url = "jdbc:sqlite:sql/fitmetrix.db";
        SQLiteDataSource dataSource = new SQLiteDataSource();
        dataSource.setUrl(url);
        Connection conn = null;

        try {
            conn = dataSource.getConnection();
        } catch (SQLException e) {
            e.printStackTrace(System.err);
        }
        return conn;
    }
    
    public void addSet(String liftTitle, Integer weight, Integer reps) {
        
        String sql = "INSERT INTO metrics(lift_id, weight, reps, intensity) VALUES(?,?,?,?)";
        
        Integer currentOneRepMax = getCurrentOneRepMax(liftTitle);
        Integer liftId = getLiftId(liftTitle);
        Integer intensity = weight / currentOneRepMax;

        Boolean newPrReached = possibleNewPR(liftTitle, weight, reps);

        if (newPrReached) {
            System.out.println("Congrats! A new PR was reached for " + liftTitle + ".");
        }

        try (
            Connection conn = this.connect();
            PreparedStatement pstmt = conn.prepareStatement(sql);
        ) {
            pstmt.setInt(1, liftId);
            pstmt.setInt(2, weight);
            pstmt.setInt(3, reps);
            pstmt.setInt(4, intensity);
            pstmt.executeUpdate();

        } catch (SQLException ex) {
            System.out.println("There was an error");
        }
    }

    public Integer getLiftId(String liftTitle) {
        String sql = "SELECT lift_id FROM lift WHERE title = ?";
        Integer liftId = null;

        try (
            Connection conn = this.connect();
            PreparedStatement pstmt= conn.prepareStatement(sql); 
        ) {
            pstmt.setString(1, liftTitle);
            ResultSet resultSet = pstmt.executeQuery();
            liftId = resultSet.getInt("lift_id");
            return liftId;

        } catch (Exception ex) {
            System.out.println("There was an error.");
        }
        return liftId;
    }

    public Integer getCurrentOneRepMax(String liftTitle) {
        String sql = "SELECT current_one_rep_max FROM lift WHERE title = ?";
        Integer currentOneRepMax = null;

        try (
            Connection conn = this.connect();
            PreparedStatement pstmt = conn.prepareStatement(sql);
        ) {
            pstmt.setString(1, liftTitle);
            ResultSet resultSet = pstmt.executeQuery();
            currentOneRepMax = resultSet.getInt("current_one_rep_max");
            return currentOneRepMax;
        } catch (Exception ex) {
            System.out.println("There was an error");
        }
        return currentOneRepMax;

    }

    public Boolean possibleNewPR(String liftTitle, Integer weight, Integer reps) {
        Integer currentOneRepMax = getCurrentOneRepMax(liftTitle);
        Integer setOneRepMax = null; 
        // TODO: Calculate one rep max

        if (setOneRepMax > currentOneRepMax) {
            updateCurrentOneRepMax(setOneRepMax);
        }
    }

    public 


}