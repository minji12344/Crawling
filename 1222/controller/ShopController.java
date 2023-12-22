package com.example.controller;

import java.util.HashMap;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.dao.ShopDAO;
import com.example.domain.QueryVO;
import com.example.domain.ShopVO;

@RestController
@RequestMapping("/shop")
public class ShopController {
	@Autowired
	ShopDAO dao;
	
	@GetMapping("/list")
	public HashMap<String, Object> list(QueryVO vo){
		HashMap<String, Object> map = new HashMap<String, Object>();
		map.put("total", dao.total());
		map.put("list", dao.list(vo));
		return map;
	}
	
	@PostMapping("/insert")
	public void insert(@RequestBody ShopVO vo) {
		dao.insert(vo);
	}
	
	@GetMapping("/read/{pid}")
	public ShopVO read(@PathVariable("pid") int pid) {
		return dao.read(pid);
	}
	
	@PostMapping("/update")
	public void update(@RequestBody ShopVO vo) {
		dao.update(vo);
	}
}
