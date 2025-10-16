<?php

namespace App\Tests\Service;

use App\Service\DiscountCalculator;
use PHPUnit\Framework\TestCase;

class DiscountCalculatorTest extends TestCase
{
    private DiscountCalculator $discountCalculator;

    protected function setUp(): void
    {
        $this->discountCalculator = new DiscountCalculator();
    }

    // Vérifie qu'aucune remise n'est appliquée si le montant est inférieur ou égal à 100 €
    public function testNoDiscountForSmallAmount(): void
    {
        $discount = $this->discountCalculator->calculateDiscount(50.0, false);
        $this->assertEquals(0.0, $discount);
    }

    // Vérifie qu'une remise de 10 % est appliquée si le montant est supérieur à 100 €
    public function testBaseDiscountForLargeAmount(): void
    {
        $discount = $this->discountCalculator->calculateDiscount(150.0, false);
        $this->assertEquals(15.0, $discount); // 10% de 150 €
    }

    // Vérifie qu'une remise supplémentaire de 5 % est appliquée pour les clients VIP
    public function testVipDiscount(): void
    {
        $discount = $this->discountCalculator->calculateDiscount(150.0, true);
        $this->assertEquals(22.5, $discount); // 10% + 5% de 150 €
    }

    // Vérifie que la remise totale ne dépasse pas 20 % du montant total
    public function testMaxDiscount(): void
    {
        $discount = $this->discountCalculator->calculateDiscount(1000.0, true);
        $this->assertEquals(150.0, $discount); // 10% + 5% de 1000 € (ne dépasse pas 20%)
    }

    // Vérifie le comportement à la limite (montant exactement égal à 100 €)
    public function testEdgeCaseExactly100(): void
    {
        $discount = $this->discountCalculator->calculateDiscount(100.0, false);
        $this->assertEquals(0.0, $discount); // Pas de remise à exactement 100 €
    }

    // Vérifie le comportement juste au-dessus de 100 €
    public function testEdgeCaseJustAbove100(): void
    {
        $discount = $this->discountCalculator->calculateDiscount(100.01, false);
        $this->assertEqualsWithDelta(10.001, $discount, 0.0001); // Tolérance de 0.0001
    }
}
