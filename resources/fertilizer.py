fertilizer_dic = {
        'NHigh': """1. Avoid over-fertilization with nitrogen-rich fertilizers, especially in areas with high rainfall.
        <br/> 2. Use slow-release nitrogen fertilizers to provide a steady supply of nitrogen to plants.
        <br/> 3. Implement cover cropping to scavenge excess nitrogen and prevent leaching.
        <br/> 4. Consider planting nitrogen-fixing plants in the rotation to utilize excess nitrogen.
        <br/> 5. Use nitrification inhibitors to slow down the conversion of ammonium to nitrate, reducing nitrogen leaching.
        <br/> 6. Practice no-till farming to reduce nitrogen loss through soil erosion.
        <br/> 7. Utilize nitrogen-fixing bacteria or fungi to enhance nitrogen availability to plants.
        <br/> 8. Apply nitrogen-fixing biofertilizers to improve soil nitrogen content naturally.
        <br/> 9. Use legume cover crops to fix atmospheric nitrogen and improve soil fertility.
        <br/> 10. Incorporate crop residues into the soil to recycle nitrogen and reduce the need for synthetic fertilizers.""",

        'NLow': """1. Conduct regular soil tests to monitor nitrogen levels and adjust fertilizer applications accordingly.
        <br/> 2. Apply nitrogen-rich organic amendments such as compost or manure.
        <br/> 3. Use leguminous cover crops or intercropping to increase nitrogen fixation.
        <br/> 4. Consider using fish emulsion or blood meal as organic nitrogen sources.
        <br/> 5. Apply nitrogen-fixing bacteria inoculants to enhance soil nitrogen availability.
        <br/> 6. Utilize green manure crops that add nitrogen to the soil as they decompose.
        <br/> 7. Use synthetic nitrogen fertilizers like urea or ammonium nitrate to quickly boost nitrogen levels.
        <br/> 8. Rotate crops with high nitrogen requirements to deplete soil nitrogen levels.
        <br/> 9. Consider using slow-release nitrogen fertilizers to provide a continuous nitrogen supply.
        <br/> 10. Apply foliar sprays of urea or other nitrogen-containing compounds to provide a quick nitrogen boost to plants.""",
        'PHigh': """1. Avoid using high-phosphorus fertilizers unless soil tests indicate a deficiency.
        <br/> 2. Use phosphorus-solubilizing microbes to enhance phosphorus availability.
        <br/> 3. Apply phosphorus in a band or localized placement to improve efficiency.
        <br/> 4. Use phosphorus-stabilizing additives to reduce phosphorus runoff.
        <br/> 5. Implement conservation tillage practices to reduce phosphorus loss through erosion.
        <br/> 6. Consider using phosphate rock or bone meal as long-term phosphorus sources.
        <br/> 7. Apply phosphorus during periods of active root growth for better uptake.
        <br/> 8. Use organic phosphorus sources like composted manure or bone meal.
        <br/> 9. Avoid applying phosphorus fertilizers to frozen or waterlogged soils.
        <br/> 10. Use mycorrhizal fungi to enhance phosphorus uptake by plants.""",

        'PLow': """1. Conduct a soil test to determine the extent of the phosphorus deficiency.
        <br/> 2. Apply phosphorus fertilizer in the fall to allow for better incorporation into the soil.
        <br/> 3. Use phosphorus fertilizer with a high percentage of water-soluble phosphorus.
        <br/> 4. Incorporate organic matter into the soil to improve phosphorus availability.
        <br/> 5. Consider using phosphorus-containing organic fertilizers such as bone meal or rock phosphate.
        <br/> 6. Apply phosphorus fertilizer in a band or trench to target plant roots.
        <br/> 7. Use mycorrhizal fungi to improve phosphorus uptake by plants.
        <br/> 8. Avoid applying phosphorus with calcium-rich materials, as this can reduce phosphorus availability.
        <br/> 9. Consider using phosphorus solubilizing bacteria to enhance phosphorus availability.
        <br/> 10. Apply phosphorus in multiple applications throughout the growing season to meet plant needs.""",

        'KHigh': """1. Avoid excessive potassium fertilization, as it can interfere with the uptake of other nutrients.
        <br/> 2. Use potassium-fixing minerals like glauconite or feldspar to reduce excess potassium levels.
        <br/> 3. Apply potassium in split doses to improve plant uptake efficiency.
        <br/> 4. Implement crop rotation with potassium-demanding crops to utilize excess potassium.
        <br/> 5. Use potassium-fixing bacteria to help regulate soil potassium levels.
        <br/> 6. Consider using potassium leaching techniques to remove excess potassium from the soil.
        <br/> 7. Apply gypsum to potassium-rich soils to improve potassium availability to plants.
        <br/> 8. Incorporate potassium into the soil before planting to ensure availability during the growing season.
        <br/> 9. Use potassium-fixing cover crops to help manage excess soil potassium.
        <br/> 10. Monitor soil potassium levels regularly to prevent excessive accumulation.""",

        'KLow': """1. Conduct a soil test to determine the extent of potassium deficiency.
        <br/> 2. Apply potassium fertilizer in early spring to promote plant growth.
        <br/> 3. Use potassium sulfate in saline soils to improve potassium availability.
        <br/> 4. Consider using potassium-rich organic materials such as wood ash or banana peels.
        <br/> 5. Apply potassium fertilizer in a band or trench to target plant roots.
        <br/> 6. Use potassium-rich biochar to improve soil structure and increase potassium retention.
        <br/> 7. Avoid excessive use of magnesium or calcium fertilizers, as they can inhibit potassium uptake.
        <br/> 8. Incorporate potassium into the soil before planting to ensure availability during the growing season.
        <br/> 9. Use foliar sprays of potassium nitrate to quickly correct potassium deficiency.
        <br/> 10. Apply potassium in multiple applications throughout the growing season to meet plant needs.""",

        'MgHigh': """1. Avoid using high magnesium fertilizers to prevent further increasing magnesium levels in the soil.
        <br/> 2. Use calcium-containing fertilizers like calcium carbonate to help reduce magnesium uptake by plants.
        <br/> 3. Apply magnesium-fixing soil amendments like greensand or langbeinite to reduce excess magnesium levels.
        <br/> 4. Consider using magnesium chelates to help plants absorb magnesium more efficiently.
        <br/> 5. Monitor soil pH, as high pH levels can increase magnesium availability to plants.
        <br/> 6. Use magnesium antagonists like potassium or ammonium to help reduce magnesium uptake by plants.
        <br/> 7. Implement drip irrigation to reduce water usage and minimize magnesium leaching.
        <br/> 8. Consider using gypsum to improve soil structure and reduce magnesium availability.
        <br/> 9. Use magnesium sulfate as a foliar spray for quick correction of magnesium deficiency in plants.
        <br/> 10. Incorporate magnesium-fixing cover crops like buckwheat or clover into the rotation to reduce soil magnesium levels.""",

'MgLow': """1. Apply dolomitic lime to raise soil magnesium levels while also adjusting pH.
        <br/> 2. Use Epsom salt (magnesium sulfate) as a quick source of magnesium for plants.
        <br/> 3. Consider using composted manure as a source of magnesium and other nutrients.
        <br/> 4. Use magnesium sulfate as a soluble source of magnesium for plants, especially in soils with low magnesium availability.
        <br/> 5. Incorporate green manures like clover or buckwheat, which can increase magnesium availability as they decompose.
        <br/> 6. Consider using magnesium chelates to improve magnesium uptake by plants.
        <br/> 7. Apply magnesium-rich rock dust or minerals to improve soil magnesium levels.
        <br/> 8. Use magnesium-containing foliar sprays to correct magnesium deficiency in plants.
        <br/> 9. Consider using magnesium oxide as a slow-release magnesium fertilizer.
        <br/> 10. Monitor plant symptoms of magnesium deficiency and adjust fertilization practices accordingly.""",
        'ZnHigh': """1. Avoid using zinc-containing fertilizers to prevent further increasing zinc levels in the soil.
        <br/> 2. Use phosphorus-containing fertilizers to balance the nutrients without adding more zinc.
        <br/> 3. Consider adding iron sulfate to induce iron chlorosis in zinc-loving plants and reduce zinc availability.
        <br/> 4. Improve soil drainage to reduce waterlogging, which can lead to zinc accumulation.
        <br/> 5. Implement crop rotation with plants that have lower zinc requirements to help deplete excess zinc in the soil.
        <br/> 6. Consider using zinc-fixing soil amendments like zinc sulfate or zinc oxide to reduce excess zinc levels.
        <br/> 7. Apply compost or organic matter to help bind excess zinc and reduce its availability to plants.
        <br/> 8. Use zinc antagonists like phosphorus or iron to reduce zinc uptake by plants.
        <br/> 9. Monitor plant symptoms of zinc toxicity and adjust fertilization practices accordingly.
        <br/> 10. Use zinc chelates to improve zinc uptake efficiency by plants.""",

'ZnLow': """1. Apply zinc sulfate as a soluble source of zinc for plants, especially in alkaline soils where zinc availability is limited.
        <br/> 2. Use organic matter such as compost or manure as a source of zinc and other micronutrients.
        <br/> 3. Consider applying composted manure, which can provide a slow-release source of zinc for plants.
        <br/> 4. Use zinc chelates, which are organic compounds that can increase the availability of zinc to plants.
        <br/> 5. Apply zinc-rich rock dust or minerals to improve soil zinc levels.
        <br/> 6. Incorporate zinc-fixing cover crops into the rotation to help increase soil zinc levels.
        <br/> 7. Use zinc-containing foliar sprays to correct zinc deficiency in plants.
        <br/> 8. Consider using zinc oxide as a slow-release zinc fertilizer.
        <br/> 9. Monitor plant symptoms of zinc deficiency and adjust fertilization practices accordingly.
        <br/> 10. Conduct a soil test to determine the exact zinc levels and adjust fertilization accordingly.""",
        'SHigh': """1. Avoid adding sulfur-containing fertilizers to prevent further increasing sulfur levels.
        <br/> 2. Use nitrogen-containing fertilizers to balance the nutrients without adding more sulfur.
        <br/> 3. Consider adding calcium-containing fertilizers such as gypsum to help balance the high sulfur levels.
        <br/> 4. Improve soil drainage to reduce waterlogging, which can lead to sulfur accumulation.
        <br/> 5. Implement crop rotation with plants that have lower sulfur requirements to help deplete excess sulfur in the soil.
        <br/> 6. Consider using sulfur-fixing soil amendments like elemental sulfur or sulfur-coated urea to reduce excess sulfur levels.
        <br/> 7. Apply compost or organic matter to help bind excess sulfur and reduce its availability to plants.
        <br/> 8. Use sulfur antagonists like nitrogen or phosphorus to reduce sulfur uptake by plants.
        <br/> 9. Monitor plant symptoms of sulfur toxicity and adjust fertilization practices accordingly.
        <br/> 10. Conduct a soil test to determine the exact sulfur levels and adjust fertilization accordingly.""",

'SLow': """1. Add elemental sulfur to raise sulfur levels in the soil, especially in alkaline soils where sulfur availability is limited.
        <br/> 2. Use gypsum as a source of sulfur and calcium for plants, especially in soils with low sulfur levels and poor soil structure.
        <br/> 3. Apply ammonium sulfate as a soluble source of sulfur for plants, especially in soils with low sulfur availability.
        <br/> 4. Incorporate sulfur-containing organic matter such as composted manure or green manures to increase sulfur levels in the soil.
        <br/> 5. Consider using sulfur-coated urea as a slow-release sulfur fertilizer for sustained sulfur availability to plants.
        <br/> 6. Use elemental sulfur in combination with microbial inoculants to enhance sulfur availability to plants.
        <br/> 7. Apply sulfur-containing foliar sprays to correct sulfur deficiency in plants.
        <br/> 8. Consider using sulfate-based fertilizers like magnesium sulfate or potassium sulfate to increase sulfur levels in the soil.
        <br/> 9. Monitor plant symptoms of sulfur deficiency and adjust fertilization practices accordingly.
        <br/> 10. Conduct a soil test to determine the exact sulfur levels and adjust fertilization accordingly."""
    }