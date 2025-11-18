<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class VerifyApiKey
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        $apiKey = $request->header('X-API-Key') ?? $request->query('api_key');
        $validApiKey = env('API_KEY');

        if (empty($validApiKey)) {
            return response()->json([
                'error' => 'API key authentication is not configured'
            ], 500);
        }

        if ($apiKey !== $validApiKey) {
            return response()->json([
                'error' => 'Invalid or missing API key'
            ], 401);
        }

        return $next($request);
    }
}

