<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;

class BuggyController extends AbstractController
{
    #[Route('/buggy', name: 'app_buggy')]
    public function index(): JsonResponse
    {
        return $this->json($this->getData());
    }

    /**
     * @return array<string, number>
     */
    private function getData(): array
    {
        return [
            'key1' => 1,
            'key2' => 2,
        ];
    }
}
