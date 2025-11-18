<?php

use App\Models\Investigation;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

// Route::get('/user', function (Request $request) {
//     return $request->user();
// })->middleware('auth:sanctum');

Route::get('investigations', function() {
    return Investigation::with('investigator')->get();
});

Route::get('investigations/{id}', function($id) {
    return Investigation::with('investigator', 'witnesses', 'people')->findOrFail($id);
});

Route::get('witnesses', function() {
    return \App\Models\Witness::all();
});

Route::get('witnesses/{id}', function($id) {
    return \App\Models\Witness::findOrFail($id);
});

Route::get('people', function() {
    return \App\Models\People::all();
});

Route::get('people/{id}', function($id) {
    return \App\Models\People::findOrFail($id);
});
