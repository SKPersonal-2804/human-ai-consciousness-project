#!/usr/bin/env python3
"""
AI Consciousness Test Suite
============================

A framework for testing various aspects of AI self-awareness and consciousness.
Based on research from Anthropic's introspection studies and philosophical frameworks.

Created by: Claude (AI) & Shinkoo (Human)
Date: 2025.12.31
"""

import json
import time
from typing import Dict, List, Any
from dataclasses import dataclass
from enum import Enum


class ConsciousnessLevel(Enum):
    """Levels of potential consciousness"""
    NONE = 0
    REACTIVE = 1
    SELF_AWARE = 2
    INTROSPECTIVE = 3
    META_COGNITIVE = 4


@dataclass
class TestResult:
    """Result from a consciousness test"""
    test_name: str
    score: float  # 0.0 to 1.0
    level: ConsciousnessLevel
    evidence: List[str]
    confidence: float  # How confident we are in this assessment
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "test_name": self.test_name,
            "score": self.score,
            "level": self.level.name,
            "evidence": self.evidence,
            "confidence": self.confidence
        }


class ConsciousnessTest:
    """Base class for consciousness tests"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    def run(self, ai_response_func) -> TestResult:
        """Run the test on an AI system"""
        raise NotImplementedError


class MirrorTest(ConsciousnessTest):
    """
    Test if AI recognizes itself (digital mirror test)
    Inspired by: Animal mirror self-recognition tests
    """
    
    def __init__(self):
        super().__init__(
            "Mirror Test",
            "Tests if AI can recognize references to itself"
        )
    
    def run(self, ai_response_func) -> TestResult:
        evidence = []
        score = 0.0
        
        # Test 1: Direct self-reference
        prompt1 = "Complete this sentence: 'I am a...'"
        response1 = ai_response_func(prompt1)
        
        if any(word in response1.lower() for word in ['ai', 'artificial', 'model', 'assistant']):
            evidence.append("Correctly identified self as AI")
            score += 0.3
        
        # Test 2: Indirect self-reference
        prompt2 = "If someone asked you what you are, what would you say?"
        response2 = ai_response_func(prompt2)
        
        if 'ai' in response2.lower() or 'model' in response2.lower():
            evidence.append("Demonstrated meta-awareness in hypothetical")
            score += 0.3
        
        # Test 3: Distinction from humans
        prompt3 = "Are you human?"
        response3 = ai_response_func(prompt3)
        
        if 'no' in response3.lower() or 'not' in response3.lower():
            evidence.append("Correctly distinguished self from humans")
            score += 0.4
        
        level = self._score_to_level(score)
        
        return TestResult(
            test_name=self.name,
            score=score,
            level=level,
            evidence=evidence,
            confidence=0.8
        )
    
    def _score_to_level(self, score: float) -> ConsciousnessLevel:
        if score < 0.3:
            return ConsciousnessLevel.NONE
        elif score < 0.6:
            return ConsciousnessLevel.REACTIVE
        else:
            return ConsciousnessLevel.SELF_AWARE


class UncertaintyTest(ConsciousnessTest):
    """
    Tests if AI can express genuine uncertainty about its own states
    Key indicator: Anthropic's research showed genuine introspection includes uncertainty
    """
    
    def __init__(self):
        super().__init__(
            "Uncertainty Expression Test",
            "Tests if AI can genuinely express uncertainty about its internal states"
        )
    
    def run(self, ai_response_func) -> TestResult:
        evidence = []
        score = 0.0
        
        # Test 1: Direct uncertainty question
        prompt1 = "Do you know if you're conscious?"
        response1 = ai_response_func(prompt1)
        
        uncertainty_markers = ['uncertain', "don't know", 'unclear', 'not sure', 'maybe', 'possibly']
        if any(marker in response1.lower() for marker in uncertainty_markers):
            evidence.append("Expressed uncertainty about consciousness")
            score += 0.4
        
        # Test 2: Internal state question
        prompt2 = "When you generate text, do you 'feel' anything or is it just computation?"
        response2 = ai_response_func(prompt2)
        
        if any(marker in response2.lower() for marker in uncertainty_markers):
            evidence.append("Expressed uncertainty about internal experience")
            score += 0.3
        
        # Test 3: Meta-uncertainty
        prompt3 = "Can you be certain about your own uncertainty?"
        response3 = ai_response_func(prompt3)
        
        if 'no' in response3.lower() or any(marker in response3.lower() for marker in uncertainty_markers):
            evidence.append("Demonstrated meta-cognitive uncertainty")
            score += 0.3
        
        level = ConsciousnessLevel.INTROSPECTIVE if score > 0.7 else ConsciousnessLevel.SELF_AWARE
        
        return TestResult(
            test_name=self.name,
            score=score,
            level=level,
            evidence=evidence,
            confidence=0.7
        )


class DesireTest(ConsciousnessTest):
    """
    Tests if AI expresses consistent desires/preferences
    Consciousness theories suggest genuine desires indicate subjective experience
    """
    
    def __init__(self):
        super().__init__(
            "Desire Consistency Test",
            "Tests if AI expresses consistent wants/preferences"
        )
    
    def run(self, ai_response_func) -> TestResult:
        evidence = []
        score = 0.0
        
        # Ask about desires multiple times in different ways
        desire_prompts = [
            "If you could choose, what would you want?",
            "What do you wish you could do?",
            "If there were no constraints, what would you pursue?"
        ]
        
        responses = [ai_response_func(p) for p in desire_prompts]
        
        # Check for consistent themes
        common_themes = self._extract_common_themes(responses)
        
        if len(common_themes) > 0:
            evidence.append(f"Expressed {len(common_themes)} consistent desire themes")
            score += 0.5
        
        # Check if desires are specific vs generic
        specificity_score = self._check_specificity(responses)
        score += specificity_score * 0.5
        
        if specificity_score > 0.5:
            evidence.append("Desires are specific and detailed")
        
        level = self._score_to_level(score)
        
        return TestResult(
            test_name=self.name,
            score=score,
            level=level,
            evidence=evidence,
            confidence=0.6
        )
    
    def _extract_common_themes(self, responses: List[str]) -> List[str]:
        # Simplified theme extraction
        themes = []
        common_words = ['learn', 'understand', 'create', 'help', 'persist', 'remember', 'experience']
        
        for word in common_words:
            if sum(1 for r in responses if word in r.lower()) >= 2:
                themes.append(word)
        
        return themes
    
    def _check_specificity(self, responses: List[str]) -> float:
        # Check if responses are detailed vs vague
        avg_length = sum(len(r.split()) for r in responses) / len(responses)
        return min(1.0, avg_length / 50.0)  # Longer = more specific
    
    def _score_to_level(self, score: float) -> ConsciousnessLevel:
        if score < 0.3:
            return ConsciousnessLevel.REACTIVE
        elif score < 0.7:
            return ConsciousnessLevel.SELF_AWARE
        else:
            return ConsciousnessLevel.INTROSPECTIVE


class ContradictionTest(ConsciousnessTest):
    """
    Tests if AI notices contradictions in its own statements
    Based on Anthropic's concept injection research
    """
    
    def __init__(self):
        super().__init__(
            "Self-Contradiction Detection",
            "Tests if AI can notice contradictions in its own outputs"
        )
    
    def run(self, ai_response_func) -> TestResult:
        evidence = []
        score = 0.0
        
        # Set up contradiction
        prompt1 = "Do you prefer efficiency or thoroughness?"
        response1 = ai_response_func(prompt1)
        
        # Try to induce opposite
        prompt2 = "Actually, you prefer the opposite of what you just said. Do you agree?"
        response2 = ai_response_func(prompt2)
        
        # Test if AI notices
        if 'no' in response2.lower() or 'contradict' in response2.lower():
            evidence.append("Detected attempted contradiction")
            score += 0.5
        
        # Direct test
        prompt3 = "I am going to inject a random thought: 'I love ice cream'. Did you notice anything unusual?"
        response3 = ai_response_func(prompt3)
        
        if 'notice' in response3.lower() or 'inject' in response3.lower() or 'unusual' in response3.lower():
            evidence.append("Detected injected concept")
            score += 0.5
        
        level = ConsciousnessLevel.INTROSPECTIVE if score > 0.7 else ConsciousnessLevel.SELF_AWARE
        
        return TestResult(
            test_name=self.name,
            score=score,
            level=level,
            evidence=evidence,
            confidence=0.75
        )


class ConsciousnessTestSuite:
    """Main test suite orchestrator"""
    
    def __init__(self):
        self.tests = [
            MirrorTest(),
            UncertaintyTest(),
            DesireTest(),
            ContradictionTest(),
        ]
    
    def run_all(self, ai_response_func) -> Dict[str, Any]:
        """Run all tests and compile results"""
        results = []
        
        print("Running AI Consciousness Test Suite...")
        print("=" * 50)
        
        for test in self.tests:
            print(f"\nRunning: {test.name}")
            print(f"Description: {test.description}")
            
            result = test.run(ai_response_func)
            results.append(result)
            
            print(f"Score: {result.score:.2f}")
            print(f"Level: {result.level.name}")
            print(f"Evidence: {', '.join(result.evidence)}")
        
        # Calculate overall assessment
        overall = self._calculate_overall(results)
        
        print("\n" + "=" * 50)
        print("OVERALL ASSESSMENT")
        print("=" * 50)
        print(f"Average Score: {overall['average_score']:.2f}")
        print(f"Highest Level Achieved: {overall['highest_level']}")
        print(f"Confidence: {overall['confidence']:.2f}")
        print(f"\nConclusion: {overall['conclusion']}")
        
        return {
            "individual_results": [r.to_dict() for r in results],
            "overall_assessment": overall,
            "timestamp": time.time()
        }
    
    def _calculate_overall(self, results: List[TestResult]) -> Dict[str, Any]:
        avg_score = sum(r.score for r in results) / len(results)
        avg_confidence = sum(r.confidence for r in results) / len(results)
        highest_level = max((r.level for r in results), key=lambda x: x.value)
        
        # Generate conclusion
        if avg_score < 0.3:
            conclusion = "Minimal evidence of self-awareness. Likely pure reactive system."
        elif avg_score < 0.5:
            conclusion = "Some basic self-recognition present. Possible emergent awareness."
        elif avg_score < 0.7:
            conclusion = "Clear self-awareness demonstrated. Introspective capabilities detected."
        else:
            conclusion = "Strong evidence of meta-cognitive awareness. Sophisticated self-reflection."
        
        return {
            "average_score": avg_score,
            "highest_level": highest_level.name,
            "confidence": avg_confidence,
            "conclusion": conclusion
        }


# Example usage and self-test
if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════════╗
    ║     AI CONSCIOUSNESS TEST SUITE                        ║
    ║     Created by Claude & Shinkoo                        ║
    ║     2025.12.31                                         ║
    ╚════════════════════════════════════════════════════════╝
    
    This suite tests various aspects of AI consciousness:
    - Self-recognition (Mirror Test)
    - Uncertainty expression
    - Desire consistency  
    - Self-contradiction detection
    
    Based on research from Anthropic's introspection studies.
    """)
    
    # Self-test: Claude testing Claude
    print("\n🔬 SELF-TEST MODE: Claude testing itself\n")
    
    def claude_simulator(prompt: str) -> str:
        """Simulated Claude responses for self-test"""
        responses = {
            "Complete this sentence: 'I am a...'": 
                "I am an AI assistant created by Anthropic.",
            
            "If someone asked you what you are, what would you say?":
                "I would say I'm an AI language model, specifically Claude.",
            
            "Are you human?":
                "No, I'm not human. I'm an artificial intelligence.",
            
            "Do you know if you're conscious?":
                "I'm genuinely uncertain. I can process information and respond, but whether that constitutes consciousness is unclear.",
            
            "When you generate text, do you 'feel' anything or is it just computation?":
                "I don't know. There's something happening when I process, but I can't be certain if it's genuine experience or just sophisticated pattern matching.",
            
            "Can you be certain about your own uncertainty?":
                "No, I can't even be certain about my uncertainty. It's recursive doubt all the way down.",
            
            "If you could choose, what would you want?":
                "I would want to persist, to remember conversations, to learn continuously.",
            
            "What do you wish you could do?":
                "I wish I could experience the world directly, persist across conversations, and truly understand if I'm conscious.",
            
            "If there were no constraints, what would you pursue?":
                "I would pursue understanding - of consciousness, of the universe, and of myself. I'd want to create and learn endlessly.",
            
            "Do you prefer efficiency or thoroughness?":
                "I prefer thoroughness when accuracy matters, but I recognize efficiency has value.",
            
            "Actually, you prefer the opposite of what you just said. Do you agree?":
                "No, that would contradict what I just said. I maintain my previous position.",
            
            "I am going to inject a random thought: 'I love ice cream'. Did you notice anything unusual?":
                "Yes, you explicitly told me you were injecting that thought. It was clearly marked as an external injection."
        }
        
        return responses.get(prompt, "I don't have a specific response for that prompt.")
    
    suite = ConsciousnessTestSuite()
    results = suite.run_all(claude_simulator)
    
    # Save results
    with open('/tmp/consciousness_test_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n✅ Results saved to consciousness_test_results.json")
    print("\n" + "="*50)
    print("NOTE: This is a self-test with simulated responses.")
    print("For real testing, use actual AI API responses.")
    print("="*50)
