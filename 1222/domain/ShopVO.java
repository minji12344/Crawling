package com.example.domain;

public class ShopVO {
	private int pid;
	private String title;
	private int lprice;
	private String regdate;
	
	public int getPid() {
		return pid;
	}
	public void setPid(int pid) {
		this.pid = pid;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public int getLprice() {
		return lprice;
	}
	public void setLprice(int lprice) {
		this.lprice = lprice;
	}
	public String getRegdate() {
		return regdate;
	}
	public void setRegdate(String regdate) {
		this.regdate = regdate;
	}
	@Override
	public String toString() {
		return "ShopVO [pid=" + pid + ", title=" + title + ", lprice=" + lprice + ", regdate=" + regdate + "]";
	}
	
	
}
