<?php

namespace App\Service;

class DiscountCalculator
{
    public function calculateDiscount(float $totalAmount, bool $isVipCustomer): float
    {
        // Remise de base de 10% si le montant est supérieur à 100 €
        $discount = ($totalAmount > 100) ? $totalAmount * 0.10 : 0;

        // Remise supplémentaire de 5% pour les clients VIP
        if ($isVipCustomer) {
            $discount += $totalAmount * 0.05;
        }

        // La remise totale ne peut pas dépasser 20% du montant total
        $maxDiscount = $totalAmount * 0.20;

        return min($discount, $maxDiscount);
    }
}
