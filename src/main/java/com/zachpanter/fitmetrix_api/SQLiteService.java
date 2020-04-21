package com.zachpanter.fitmetrix_api;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import org.springframework.stereotype.Service;

import org.sqlite.SQLiteDataSource;

@Service
public class SQLiteService {

    public SQLiteService() {
        connect();
    }

    public static void connect() {

        String url = "jdbc:sqlite:sql/fitmetrix.db";
        SQLiteDataSource dataSource = new SQLiteDataSource();
        dataSource.setUrl(url);

        try (Connection conn = dataSource.getConnection()) {
            System.out.println("Connected.");
            String sql = "SELECT * FROM lift;";
            try (
                Statement s = conn.createStatement();
                ResultSet rs = s.executeQuery(sql)) {
                
                while (rs.next()) {
                    // Read the results set
                    System.out.println("title = " + rs.getString("title"));
                }


            } catch (SQLException e) {
            e.printStackTrace(System.err);
            } 
        } catch (Exception ex) {
            System.out.println("The connection was unsuccessful.");
        }
    }   
}