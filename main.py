import asyncio
import time
from agents.analyst import StrategicAnalyst
from agents.simulator import ScenarioSimulator
from agents.auditor import RiskAuditor
from agents.resource_manager import ResourceManager
from agents.controller import DecisionController

__author__ = "Jiaming"
__version__ = "1.0.0-prototype"


async def run_strategic_decision_system(goal: str):
    print("=" * 60)
    print(f"[SYSTEM START] Initializing MAS Strategic Decision System")
    print(f"[TARGET] Strategic Goal: {goal}")
    print("=" * 60)

    # 1. Instantiate the 5 Core Agents
    analyst = StrategicAnalyst("Agent_Analyst", "Data Retrieval & Market Analysis")
    simulator = ScenarioSimulator("Agent_Simulator", "Game Theory & Scenario Modeling")
    auditor = RiskAuditor("Agent_Auditor", "Critic & Compliance Checking")
    resource_mgr = ResourceManager("Agent_Resource", "Resource Optimization")
    controller = DecisionController("Agent_Controller", "Global Orchestration")

    start_time = time.time()

    # 2. Parallel Execution: Perception & Simulation Layer
    print("\n[Phase 1] Parallel Perception & Simulation")
    analysis_task = asyncio.create_task(analyst.execute_task({"strategic_goal": goal}))
    simulation_task = asyncio.create_task(simulator.execute_task({"strategic_goal": goal}))

    res_analysis, res_simulation = await asyncio.gather(analysis_task, simulation_task)
    print(f"  -> Analyst Output: {res_analysis}")
    print(f"  -> Simulator Output: {res_simulation}")

    # 3. Sequential Execution: Constraint & Audit Layer
    print("\n[Phase 2] Resource Constraints & Risk Auditing")
    res_resource = await resource_mgr.execute_task(res_simulation)
    res_audit = await auditor.execute_task(res_analysis)
    print(f"  -> Resource Output: {res_resource}")
    print(f"  -> Auditor Output: {res_audit}")

    # 4. Controller Execution: Synthesis & Protocol Verification
    print("\n[Phase 3] Controller Synthesis & Protocol Verification")
    global_constraints = {"max_budget": 8000000, "risk_tolerance": 0.8}

    final_result = await controller.execute_task({
        "proposals": [res_simulation, res_audit, res_resource],
        "constraints": global_constraints
    })

    print("\n" + "=" * 60)
    if final_result["status"] == "success":
        print(f"[SUCCESS] System Output: {final_result['final_strategy']}")
    else:
        print(f"[FAILED] System Action: {final_result['action']} ({final_result['reason']})")

    print(f"[METRIC] Total Execution Time: {time.time() - start_time:.2f} seconds")
    print("=" * 60)


if __name__ == "__main__":
    strategic_goal = "2026 AI Enterprise Transformation & Market Entry"
    asyncio.run(run_strategic_decision_system(strategic_goal))