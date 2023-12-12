package com.example.ex02;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import androidx.annotation.Nullable;

public class DBHelper extends SQLiteOpenHelper {
    public DBHelper(@Nullable Context context) {
        super(context, "product.db", null, 1);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("create table product(_id integer primary key autoincrement, name text, price integer)");
        db.execSQL("insert into product(name, price) values('김아름', 1000)");
        db.execSQL("insert into product(name, price) values('박선우', 2000)");
        db.execSQL("insert into product(name, price) values('김민지', 3000)");
        db.execSQL("insert into product(name, price) values('김병무', 500)");

    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("drop table if exists product");
        onCreate(db);
    }
}
