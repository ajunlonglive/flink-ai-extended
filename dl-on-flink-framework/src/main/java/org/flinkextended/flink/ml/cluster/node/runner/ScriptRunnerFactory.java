/*
 * Copyright 2022 Deep Learning on Flink Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.flinkextended.flink.ml.cluster.node.runner;

import org.flinkextended.flink.ml.cluster.node.MLContext;
import org.flinkextended.flink.ml.cluster.node.runner.python.ProcessPythonRunner;
import org.flinkextended.flink.ml.util.MLConstants;
import org.flinkextended.flink.ml.util.MLException;
import org.flinkextended.flink.ml.util.ReflectUtil;

import java.lang.reflect.InvocationTargetException;

/** A factory for ScriptRunner. */
public class ScriptRunnerFactory {

    private ScriptRunnerFactory() {}

    /**
     * @param mlContext machine learning cluster node context
     * @return ScriptRunner
     * @throws MLException
     */
    public static ScriptRunner getScriptRunner(MLContext mlContext) throws MLException {
        String impl = mlContext.getProperties().get(MLConstants.SCRIPT_RUNNER_CLASS);
        // default to process scriptRunner
        if (impl == null) {
            impl = ProcessPythonRunner.class.getCanonicalName();
        }
        Class[] classes = new Class[1];
        classes[0] = MLContext.class;
        Object[] objects = new Object[1];
        objects[0] = mlContext;
        try {
            return ReflectUtil.createInstance(impl, classes, objects);
        } catch (IllegalAccessException
                | InvocationTargetException
                | InstantiationException
                | NoSuchMethodException
                | ClassNotFoundException e) {
            e.printStackTrace();
            throw new MLException("Failed to create script scriptRunner", e);
        }
    }
}
